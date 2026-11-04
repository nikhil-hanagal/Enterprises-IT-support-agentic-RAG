from pathlib import Path

root=Path(".")

# create the folders
folders=[
    "app/aip",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads"
    "tests"
]

# create the files

files=[
    "app/main.py",
    "ingent_sample_kb.py",
    "run.py",
    ".env",
]

for folder in folders:
    (root/folder).mkdir(parents=True, exist_ok=True)

for file in files:
    (root/file).touch(exist_ok=True)

print("Project structure created successfully.")