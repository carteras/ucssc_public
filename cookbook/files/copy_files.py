from pathlib import Path
import shutil

def copy_file_append_incrementor(source, destination):
    source = Path(source)
    destination = Path(destination)
    output_path = Path(destination.parent)
    output_path.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        shutil.copy(source, destination)
    else:
        inc = 1
        while True:
            new_file = f'{destination.stem}_{inc}{destination.suffix}'
            inc += 1
            if not Path(output_path / new_file).exists():
                break
        shutil.copy(source, output_path / new_file)

cmds = "test_1.txt out/test_1.txt"
cmd_source, cmd_destination = cmds.split(" ")

copy_file_append_incrementor(cmd_source, cmd_destination)