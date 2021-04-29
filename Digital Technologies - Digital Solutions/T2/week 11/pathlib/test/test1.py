from pathlib import Path

digital_tech_path = Path(r'Digital Technologies - Digital Solutions\T2\week 11\pathlib\test')
file_source = 'foo/'
file_name = 'animal.jpg'
file_path = digital_tech_path / file_source / file_name

destination = digital_tech_path / Path("temp/")

destination.mkdir(parents=True, exist_ok=True)
destination_file = destination / file_name

destination_file.write_bytes(file_path.read_bytes())

# destination_file.unlink()

files = destination.glob('*\.')
for f in files:
    if f.is_file():
        print(f)
