from csv import reader
from os import walk
import pygame
import os
import sys

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        img_files.sort(reverse = False)
        for image in img_files:
            full_path = resource_path(path + '/' + image)
            image_surface = pygame.image.load(full_path).convert_alpha()
           # print(f"Loaded image: {full_path}")
            surface_list.append(image_surface)
    return surface_list


       # ground_image_path = resource_path("graphics/tilemap/ground.png")
        #self.ground_image = pygame.image.load(ground_image_path).convert_alpha()


# Get the path to the bundled resources
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
       # base_path = sys._MEIPASS
       base_path = getattr(sys, 'MEIPASS',os.path.dirname(os.path.abspath(__file__)))
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)