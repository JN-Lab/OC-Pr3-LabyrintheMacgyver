#! /usr/bin/env python3
# coding: utf-8

import os
import json


class Character:
    """ This class creates the characters for the game """

    MIN_X_POSITION = 0
    MAX_X_POSITION = 15
    MIN_Y_POSITION = 0
    MAX_Y_POSITION = 15

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.face = 'X'

    def move(self):
        pass

    def get_items(self):
        pass

class Level:
    """ This class creates the Labyrinth which will be used for the game
    from a Json file located in the folder named sources/ """

    def __init__(self, data_file, key):
        """ Give the different attributes to the object """
        self.data_file = data_file
        self.key = key # It is the attribute in Json file
        self.structure = []

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

    def print_labyrinth_into_terminal(self):
        """ This function print the labyrinth into the terminal """

        for line in self.structure:
            line = ''.join(line)
            print(line)


def main():
    """ main function of the program """
    # Welcome message
    print("\n##########")
    print("Aidez MacGyver à s'échapper du labyrinthe")
    print("##########\n")

    # Ask play?

    # Initialization of the labyrinth
    labyrinth = Level('labyrinthe.json', 'line')
    labyrinth.generate_labyrinth_from_json()

    # Initialization of MacGyver
    macgyver = Character(1, 1)
    labyrinth.structure[1][1] = macgyver.face

    # Print labyrinth with Mac Gyver on its initial position
    labyrinth.print_labyrinth_into_terminal()



if __name__ == "__main__":
    main()
