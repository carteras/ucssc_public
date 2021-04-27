from pathlib import Path
p = Path("temp/")
p.mkdir(parents=True, exist_ok=True)
fn = "test.txt" # I don't know what is your fn
filepath = p / fn
with filepath.open("w", encoding ="utf-8") as f:
    f.write(result)