import glob
import os
import sys

block_cipher = None

def find_files(base_dir, pattern):
    """ Recursively find all files matching the pattern in the base_dir. """
    files = []
    for file in glob.glob(os.path.join(base_dir, pattern), recursive=True):
        if os.path.isfile(file):
            # Create tuple (source, destination)
            rel_path = os.path.relpath(file, base_dir)
            dest_dir = os.path.dirname(rel_path)
            
            # Append tuple (source, destination directory)
            files.append((file, dest_dir))
    return files

# Base directory of your project
base_dir = os.path.abspath('.')

# Patterns to include
patterns = [
    'graphics/**/*.png',
    'graphics/font/*.ttf',
    'map/*.csv',
    'audio/**/*.wav',
    'audio/*'
]

# Generate the datas list
datas = []
for pattern in patterns:
    datas.extend(find_files(base_dir, pattern))


# Get the path to the bundled resources
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    data_files = datas
    print(data_files)