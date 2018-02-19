#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import json

import pygame

class Level:
    """ This class creates the Labyrinth which will be used for the game
    from a Json file located in the folder named sources/ """

    MIN_Y_AXIS = 0
    MAX_Y_AXIS = 14
    MIN_X_AXIS = 0
    MAX_X_AXIS = 14

    def __init__(self, data_file, key):
        """ This method gives the different attributes to the Level's labyrinth """
        self.data_file = data_file
        self.key = key # It is the attribute in Json file
        self.structure = []

        self.generate_labyrinth_from_json()

    def generate_labyrinth_from_json(self):
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

    def print_level(self, screen):
        """ this method loads the labyrinth """
        wall_images = pygame.image.load("sources/wall-tiles-40x40.png").convert_alpha()
        zone = pygame.Surface((40, 40))

        num_line = 0
        for line in self.structure:
            num_stripe = 0
            for stripe in line:
                x_case = num_stripe * 40
                y_case = num_line * 40
                if stripe == "#":
                    zone.blit(wall_images, (0, 0), (300, 20, 40, 40))
                    screen.blit(zone, (x_case, y_case))
                else:
                    zone.blit(wall_images, (0, 0), (100, 0, 40, 40))
                    screen.blit(zone, (x_case, y_case))
                num_stripe += 1
            num_line += 1
