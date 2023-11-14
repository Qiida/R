from pathlib import Path
from os.path import join

ROOT_DIR = str(Path(__file__).parent.parent)
RESOURCES_DIR = join(ROOT_DIR, "resources")
DATA_DIR = join(ROOT_DIR, "data")

if __name__ == '__main__':
    print(ROOT_DIR)
    print(RESOURCES_DIR)
    print(DATA_DIR)
    