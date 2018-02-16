#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import json


class Character:
    """ This class creates the characters for the game """

    MIN_X_POSITION = 0
    MAX_X_POSITION = 15
    MIN_Y_POSITION = 0
    MAX_Y_POSITION = 15

    def __init__(self, x_position, y_position, labyrinth_structure):
        self.x_position = x_position
        self.y_position = y_position
        self.face = 'X'
        self.direction = ""
        self.labyrinth_structure = labyrinth_structure

        # Locate the character inside the structure and print it.
        self.labyrinth_structure[self.y_position][self.x_position] = self.face

    def move(self, direction):
        """ This method allows the character to move on the top, the right, the bottom
        or the left if there is no wall. At the same time, it manages the evolution
        of the structure according the movement of the main character """

        print("\n La direction que tu as choisie: {}\n".format(direction))

        if direction == "droite":
            if self.labyrinth_structure[self.y_position][self.x_position + 1] == "O":
                self.labyrinth_structure[self.y_position][self.x_position] = "O"
                self.x_position += 1
                self.labyrinth_structure[self.y_position][self.x_position] = self.face
            else:
                if self.labyrinth_structure[self.y_position][self.x_position + 1] == "#":
                    print("Pas possible. C'est un mur!")
                else:
                    print("Bravo!! Tu as trouvé la sortie.")
                    sys.exit()
        elif direction == "gauche":
            if self.labyrinth_structure[self.y_position][self.x_position - 1] == "O":
                self.labyrinth_structure[self.y_position][self.x_position] = "O"
                self.x_position -= 1
                self.labyrinth_structure[self.y_position][self.x_position] = self.face
            else:
                if self.labyrinth_structure[self.y_position][self.x_position + 1] == "#":
                    print("Pas possible. C'est un mur!")
                else:
                    print("Bravo!! Tu as trouvé la sortie.")
                    sys.exit()
        elif direction == "haut":
            if self.labyrinth_structure[self.y_position - 1][self.x_position] == "O":
                self.labyrinth_structure[self.y_position][self.x_position] = "O"
                self.y_position -= 1
                self.labyrinth_structure[self.y_position][self.x_position] = self.face
            else:
                if self.labyrinth_structure[self.y_position][self.x_position + 1] == "#":
                    print("Pas possible. C'est un mur!")
                else:
                    print("Bravo!! Tu as trouvé la sortie.")
                    sys.exit()
        elif direction == "bas":
            if self.labyrinth_structure[self.y_position + 1][self.x_position] == "O":
                self.labyrinth_structure[self.y_position][self.x_position] = "O"
                self.y_position += 1
                self.labyrinth_structure[self.y_position][self.x_position] = self.face
            else:
                if self.labyrinth_structure[self.y_position][self.x_position + 1] == "#":
                    print("Pas possible. C'est un mur!")
                else:
                    print("Bravo!! Tu as trouvé la sortie.")
                    sys.exit()
        else:
            print("La commande n'est pas correcte. Veuillez réessayer.")

        self.print_labyrinth_into_terminal()

    def print_labyrinth_into_terminal(self):
        """ This method prints the labyrinth. It is a method from the Character's class
        - end not from the level class - because it allows to get the labyrinthe structure
        updated with the movement of the characters """

        for line in self.labyrinth_structure:
            line = ''.join(line)
            print(line)

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


def main():
    """ main function of the program """
    # Welcome message
    print("\n##########")
    print("Aidez MacGyver à s'échapper du labyrinthe")
    print("##########\n")

    # Initialization of the labyrinth
    labyrinth = Level('labyrinthe.json', 'line')
    labyrinth.generate_labyrinth_from_json()

    # Initialization of MacGyver
    macgyver = Character(1, 1, labyrinth.structure)

    # Print labyrinth with Mac Gyver on its initial position
    macgyver.print_labyrinth_into_terminal()

    # Start game
    while True:
        print("\n ----------")
        direction = input("Dans quel direction souhaitez-vous diriger MacGyver?\n Tapez droite pour aller à droite \n Tapez gauche pour aller à gauche \n Tapez haut pour aller en haut \n Tapez bas pour aller en bas \n Votre choix : ")
        direction = direction.lower()
        print("----------\n")

        macgyver.move(direction)

if __name__ == "__main__":
    main()
