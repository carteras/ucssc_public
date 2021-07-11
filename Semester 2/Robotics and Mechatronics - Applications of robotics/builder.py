from pathlib import Path

directories = [
    '.admin',
    '.foo',
    'week1-1', 
    'week16-16'
]
here = Path("2021\Robotics and Mechatronics - Applications of robotics")

weeks = [2, 3]
for i in range(2, 15, 2):
    directories.append(f'week{weeks[0]}-{weeks[1]}')
    weeks = [x+2 for x in weeks]

for directory in directories: 
    new_dir = here / directory
    new_dir.mkdir(parents=True)
