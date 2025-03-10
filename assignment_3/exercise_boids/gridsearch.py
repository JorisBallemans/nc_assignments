import itertools
import subprocess

a = [0, 0.5, 1]
s = [0, 0.5, 1]
c = [0, 0.5, 1]

combinations = list(itertools.product(a, s, c))
print(combinations)
for combination in combinations:
    subprocess.run(['./run.sh', str(50), str(10), str(25) ,str(combination[0]), str(combination[1]), str(combination[2])])