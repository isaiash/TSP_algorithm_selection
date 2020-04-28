import subprocess

def run_command(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
N_CITIES = 3000
MAX_CITIES = 1000000
X=(MAX_CITIES-N_CITIES*10)**(1/N_CITIES)
exp = [int(i*10+X**i) for i in range(1,N_CITIES+1)]

for i, N in enumerate(exp[395:]):
    print(i,N)
    run_command("Rscript test.R "+str(N))
