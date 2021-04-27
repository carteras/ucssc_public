from pathlib import Path

digital_technologies_path = Path("Digital Technologies - Digital Solutions/T2/week 11/pathlib/test/")

print('-'*50)
with open(digital_technologies_path / 'foo.txt' , 'r') as fr:
    for line in fr:
        line = line.strip()
        print(line)