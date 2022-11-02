from pathlib import Path

data = Path("index.html").read_text().replace('\n', ' ')
print(data)