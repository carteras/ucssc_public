from pathlib import Path
directories = [Path().cwd()]

def walk(directory_name):
    for path_object in directory_name.glob("*/*"):
        if path_object.is_file(): 
            print(f'Hey, {path_object} is a file!')
        elif path_object.is_dir():
            directories.append(path_object)
            # if path_object not in directories:
                

while len(directories) > 0:
    directory = directories.pop(0)
    walk(directory)

