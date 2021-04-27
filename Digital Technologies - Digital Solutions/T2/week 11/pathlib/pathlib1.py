from pathlib import Path 

files = Path.cwd().glob('*\.')
for f in files:
    if f.is_file():
        print(f)