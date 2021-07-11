from pathlib import Path

here = Path('2021\Semester 2\Digital Technologies - Scaffolded Project\week1-1')
names = []
scores = []
with open(here/'students.txt', 'r') as fr:
    for line in fr:
        line = line.strip().split(': ')
        names.append(line[0])
        scores.append(int(line[1]))
import statistics
print(max(scores))
print(statistics.mean(scores))
print(statistics.mode(scores))
print(min(scores))

