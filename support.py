from os import walk#lets us walk through different folders
import pygame

def import_folder(path):
    surface_list = []

    for _,_, img_files in walk(path): #walk through each folder
        for image in img_files:#walk through each file in the folder
            full_path = path + '/'+ image#get the full path for each image
            image_surf = pygame.image.load(full_path).convert_alpha()#create pygame surface
            surface_list.append(image_surf)#add it to our list of surfaces
            print(image)

    return surface_list
