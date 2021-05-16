from pathlib import Path

pathlib_working_path = Path(r"Digital Technologies - Digital Solutions\T2\week 11\pathlib\test")

file_path = 'foo/'

file_name = 'animal.jpg'
# file_name = 'foo2.txt'

animal_path = pathlib_working_path/file_path/file_name

destination = pathlib_working_path / "temp/"

destination_file = destination / file_name
# print(destination_file)
destination.mkdir(parents=True, exist_ok=True), 
destination_file.write_bytes(animal_path.read_bytes())

files = list(destination.glob('**/*'))
for f in files:
    print(f)

print(Path.cwd())