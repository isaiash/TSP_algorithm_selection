def init():
    global RESULTS_PATH
    global DATASET_PATH
    global SOLVERS
    global SOLVERS_NAME
    global DATASETS
    global MAX_INT
    
    RESULTS_PATH = "RESULTS/"
    DATASET_PATH = "DATASET/PUBLIC/"
    SOLVERS = [
        #"GREEDY",
        "CLK",
        "LKH",
        "CONCORDE",
        "EAX",
        "MAOS",
    ]
    SOLVERS_NAME = [
        "Chained Lin-Kernighan",
        "Lin-Kernighan-Helsgaun",
        "Concorde",
        "Edge Assembly Crossover",
        "Multiagent optimization system"
    ]
    DATASETS = {
        "TSPLIB",
        "TNM",
        "NATIONAL",
        "VLSI",
        "NETGEN",
        "NETGENM",
        "RUE",
        "ART",
        "TSPGEN"
    }
    MAX_INT = 9223372036854775807