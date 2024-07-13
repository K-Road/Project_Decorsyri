import glob
import os
import sys

def find_files(pattern):
    """ Recursively find all files matching the pattern. """
    return glob.glob(pattern, recursive=True)

def generate_data_files():
    added_files = [
        ('README.md', '.'),
        ('graphics/**/*.png', 'graphics/*'),
        ('graphics/font/**/*.ttf', '.'),
        ('map/**/*.csv', '.'),
        ('audio/**/*.wav', '.')
    ]

    data_files = []

    for source_pattern, destination in added_files:
        for file_path in find_files(source_pattern):
            if os.path.isfile(file_path):  # Only add files, not directories
                # Create a tuple with the full source path and destination directory
                data_files.append((os.path.abspath(file_path), os.path.join(destination, os.path.basename(file_path))))

    return data_files

# Get the path to the bundled resources
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    data_files = generate_data_files()
    print(data_files)