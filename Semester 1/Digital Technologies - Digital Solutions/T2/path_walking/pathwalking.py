from pathlib import Path

root_directory = Path().cwd()

directories = []
directories.append(root_directory)

files = {}

def walk(directory_name):
    for path_object in directory_name.glob('**/*'):
        if path_object.is_file():
            files[path_object.name] = path_object
        elif path_object.is_dir():
            if path_object not in directories:
                directories.append(path_object)    
            
while len(directories) > 0:
    directory = directories.pop(0)
    walk(directory)

for key in files:
    print(f'{key}\t{files[key]}')
