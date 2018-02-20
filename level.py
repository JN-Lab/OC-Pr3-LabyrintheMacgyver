#! /usr/bin/env python3
# coding: utf-8

import os
import json

import pygame

class Level:
    """ This class creates the Labyrinth which will be used for the game
    from a Json file located in the folder named sources/ """

    def __init__(self, data_file, key):
        """ This method gives the different attributes to the Level's labyrinth """
        self.data_file = data_file
        self.key = key # It is the attribute in Json file
        self.structure = []
        self.wall_images = pygame.image.load("sources/wall-tiles-40x40.png").convert_alpha()
        self.floor_images = pygame.image.load("sources/floor-tiles-20x20.png").convert_alpha()

        self.__generate_labyrinth_from_json()

    def __generate_labyrinth_from_json(self):
        """ This function loads the labyrinth's structure into a list
        containing each line. Each line is a list containing each stripe.
        example : structure = [[stripe1_from_line1, stripe2_from_line1,...],
        [stripe1_from_line2, stripe2_from_line2,...],...] """

        labyrinth_structure = []

        directory = os.path.dirname(__file__) # We get the right path
        path_to_file = os.path.join(directory, 'sources', self.data_file) # We build the path

        try:
            with open(path_to_file, "r") as file:
                data = json.load(file)
                for lines in data:
                    labyrinth_lines = []
                    for stripe in lines[self.key]:
                        labyrinth_lines.append(stripe)
                    labyrinth_structure.append(labyrinth_lines)

            self.structure = labyrinth_structure
        except FileNotFoundError as error_message:
            print("The file was not found. Here is the original message : ", error_message)
        except:
            print("Destination unknown")
