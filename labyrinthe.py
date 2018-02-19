#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import json
import random

import pygame

class Character:
    """ This class creates the characters for the game """

    def __init__(self, x_position, y_position, face):
        """ This method gives the different attributes to the character's object """
        self.x_position = x_position
        self.y_position = y_position
        self.face = face
        self.numb_items = 0
        self.direction = ""

    def move(self, direction, labyrinth_structure):
        """ This method allows the character to move on the top, the right, the bottom
        or the left if there is no wall. At the same time, it manages the evolution
        of the structure according the movement of the main character. If the
        character reachs the F case, he wins. """

        self.direction = direction
        next_case_face = ""

        if direction == "droite":
            next_case_face = labyrinth_structure[self.y_position][self.x_position + 1]
            if next_case_face != "#":
                self.x_position += 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "gauche":
            next_case_face = labyrinth_structure[self.y_position][self.x_position - 1]
            if next_case_face != "#":
                self.x_position -= 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "haut":
            next_case_face = labyrinth_structure[self.y_position - 1][self.x_position]
            if next_case_face != "#":
                self.y_position -= 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "bas":
            next_case_face = labyrinth_structure[self.y_position + 1][self.x_position]
            if next_case_face != "#":
                self.y_position += 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        else:
            print("La commande n'est pas correcte. Veuillez réessayer.")

    def __touch(self, face_item):
        """ This private method manages the interaction between character and objects
        after the movement of the main character """
        if face_item == "F":
            if self.numb_items < 3:
                print("Perdu! Le gardien t'a attrappé.")
            else:
                print("Bravo!! MacGyver a pu s'échapper.")
            sys.exit()
        else:
            self.numb_items += 1

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

class Object:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self, face):
        """ This method gives the attribute to the Object's item """
        self.x_position = 0
        self.y_position = 0
        self.face = face
        self.direction = ""

    def get_position(self, labyrinth_structure):
        """ This method selects a random valid place in the labyrinth
         to get object position """
        valid_location = []
        for index_line, line in enumerate(labyrinth_structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == "O":
                    valid_location.append([index_line, index_stripe])
                else:
                    pass
        winner_location = random.choice(valid_location)
        self.y_position = winner_location[0]
        self.x_position = winner_location[1]

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))

    screen_play = pygame.Surface((600, 600))
    labyrinth = Level("labyrinthe.json", "line")

    game = 1
    while game:
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 1000, 1000))
        window.blit(screen_play, (200, 200))
        labyrinth.print_level(screen_play)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game = 0
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
