import numpy as np
from os import listdir
from collections import defaultdict
import config
import matplotlib.pyplot as plt

config.init()
RESULTS_PATH = config.RESULTS_PATH
DATASET_PATH = config.DATASET_PATH
SOLVERS = config.SOLVERS
SOLVERS_NAME = config.SOLVERS_NAME
DATASETS = config.DATASETS
MAX_INT = config.MAX_INT

def create_timesteps(n_seconds, n_timesteps):
    timesteps = np.logspace(1, 20, num=n_timesteps+1, base=2)-2 # escala logaritmica para los tiempos
    timesteps = n_seconds*timesteps/timesteps.max()
    timesteps = timesteps[1:]
    return timesteps

# Dataset names
def get_dataset_files():
    dataset_files = defaultdict(list)
    for dataset in DATASETS:
        for instance_file in [f for f in listdir(DATASET_PATH+dataset)]:
            dataset_files[dataset].append(instance_file)
    return dataset_files

# Get sizes
def get_size(filepath):
    f = open(filepath)
    for line in f:
        split_ = line.split()
        if split_[0] == 'DIMENSION':
            return int(split_[2])
        elif split_[0] == 'DIMENSION:':
            return int(split_[1])

def get_dataset_sizes():
    dataset_sizes = defaultdict(dict)
    for dataset in DATASETS:
        for instance_file in [f for f in listdir(DATASET_PATH+dataset)]:
            dataset_sizes[dataset][instance_file] = get_size(DATASET_PATH+dataset+'/'+instance_file)
    return dataset_sizes

def read_file(file):
    info = []
    for f in file:
        split_ = f.split()
        if len(split_) != 2:
            continue
        if split_[0] == 'infeas_recover':
            continue
        if split_[0][0] == '-':
            split_[0] = split_[0].replace("-", "")
        obj_value,time = int(split_[0]), float(split_[1])
        if len(info) > 0:
            if info[-1][0] < obj_value or info[-1][1] > time:
                continue
            else:
                info.append([obj_value,time])
        else:
            info.append([obj_value,time])
    return info

#Instance Framing
def read_dataset_file(dataset, filename):
    points = []
    filepath = DATASET_PATH+dataset+'/'+filename
    f = open(filepath)
    read = 0
    for line in f:
        if line == 'NODE_COORD_SECTION\n' or line == 'NODE_COORD_SECTION \n':
            read = 1
            continue
        if read and line != 'EOF\n'and line != ' EOF\n'and line != 'EOF \n' and line != '\n' and line != "EOF":
            points.append([float(line.split()[1]), float(line.split()[2])])
    f.close()
    return np.array(points)

def get_frame(points, n_grid):
    x_min, x_max, y_min, y_max = points[:,0].min(), points[:,0].max(), points[:,1].min(), points[:,1].max()
    points[:,0] = (points[:,0] - x_min)/(x_max - x_min)
    points[:,1] = (points[:,1] - y_min)/(y_max - y_min)
    frame = np.zeros((n_grid,n_grid))
    for p in points:
        x_position, y_position = int(p[0] * n_grid-1), int(p[1] * n_grid-1)
        frame[x_position][y_position] += 1
    return frame

def visualize_frame(dataset_,instance_,N_grid):
    p = read_dataset_file(dataset_,instance_)
    plt.scatter(p[:,0],p[:,1])
    plt.show()
    # Normalize
    x_min, x_max, y_min, y_max = p[:,0].min(), p[:,0].max(), p[:,1].min(), p[:,1].max()
    p[:,0] = (p[:,0] - x_min)/(x_max - x_min)
    p[:,1] = (p[:,1] - y_min)/(y_max - y_min)
    plt.scatter(p[:,0],p[:,1])
    plt.show()
    # Framing
    frame = np.zeros((N_grid,N_grid))
    for point in p:
        x_position, y_position = int(point[0] * N_grid-1), int(point[1] * N_grid-1)
        frame[x_position][y_position] += 1
    plt.imshow(frame.T, cmap='gray_r', vmin=0, vmax=frame.max())
    plt.show()

#cruce de lineas
'''
INSTANCE = 'Tnm1000.tsp.out'
fig=plt.figure(figsize=(18, 10), dpi= 80, facecolor='w', edgecolor='k')
for SOLVER in SOLVERS:
    x = np.array(solvers_data[SOLVER][INSTANCE])
    print(SOLVER, len(x))
    plt.plot(x[:,1], x[:,0])

x1,x2,y1,y2 = plt.axis()
limits = (0,10,y1+6350000,y2-134000000)
print(limits)
plt.axis(limits)
plt.show()
'''
def get_timeline_per_solver(result_data, timesteps, solver_,dataset_,file_):
    timeline = []
    ts_ix = 0
    current_best = [MAX_INT, 0]
    for data in result_data[solver_][dataset_][file_]:
        while timesteps[ts_ix] <= data[1]:
            timeline.append(current_best)
            ts_ix += 1
        if data[0] < current_best[0]:
            current_best = data
    if ts_ix < len(timesteps):
        for i in range(len(timesteps)-ts_ix):
            timeline.append(current_best)
    return timeline

def sort_by_size(dataset_):
    files_ = []
    sizes_ = []
    for i in dataset_sizes[dataset_]:
        files_.append(i)
        sizes_.append(dataset_sizes[dataset_][i])
    return np.array(files_)[np.array(sizes_).argsort()]

def sort_all():
    files_ = []
    sizes_ = []
    for dataset_ in DATASETS:
        for i in dataset_sizes[dataset_]:
            files_.append(i)
            sizes_.append(dataset_sizes[dataset_][i])
    return np.array(files_)[np.array(sizes_).argsort()]

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def plot_matrix():
    #matrix = np.zeros((len(timesteps), len(complete_dataset)))
    matrix = []
    for dataset_ in dataset_files.keys():
        #dataset_sorted = sort_by_size(dataset_)
        for f in dataset_files[dataset_]:
            count = 0
            files_count = 0
            for solver_ in SOLVERS:
                if f in result_data[solver_][dataset_].keys():
                    count += 1
            if count == len(SOLVERS):
                new_array = []
                for i,time in enumerate(timesteps):
                    rank = get_ranking(dataset_, f, i)
                    if rank == -1:
                        new_array.append(0)
                    else:
                        new_array.append(rank[0]+1)
                files_count+=1
                matrix.append(new_array)
    matrix = np.array(matrix)
    matrix.shape