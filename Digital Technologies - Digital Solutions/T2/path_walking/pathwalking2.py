from pathlib import Path 

def walk(directory_name):
    for path_object in directory_name.glob("**/*"):
        if path_object.is_file():
            print(f"{path_object}")
        elif path_object.is_dir():
            if path_object not in directories:
                directories.append(path_object)

start_directory = Path().cwd()

directories = [start_directory]

while len(directories) > 0:
    directory = directories.pop(0)
    walk(directory)


