from pathlib import Path

data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
print(output)