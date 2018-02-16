#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import json


class Character:
    """ This class creates the characters for the game """

    def __init__(self, x_position, y_position, face):
        self.x_position = x_position
        self.y_position = y_position
        self.face = face
        self.direction = ""

    def move(self, direction, labyrinth_structure):
        """ This method allows the character to move on the top, the right, the bottom
        or the left if there is no wall. At the same time, it manages the evolution
        of the structure according the movement of the main character. If the
        character reachs the F case, he wins. """

        self.direction = direction

        if direction == "droite":
            if labyrinth_structure[self.y_position][self.x_position + 1] == "O":
                self.x_position += 1
            else:
                if labyrinth_structure[self.y_position][self.x_position + 1] == "F":
                    self.escape_success()
                else:
                    print("Pas possible. C'est un mur!\n")
        elif direction == "gauche":
            if labyrinth_structure[self.y_position][self.x_position - 1] == "O":
                self.x_position -= 1
            else:
                if labyrinth_structure[self.y_position][self.x_position - 1] == "F":
                    self.escape_success()
                else:
                    print("Pas possible. C'est un mur!\n")
        elif direction == "haut":
            if labyrinth_structure[self.y_position - 1][self.x_position] == "O":
                self.y_position -= 1
            else:
                if labyrinth_structure[self.y_position - 1][self.x_position] == "F":
                    self.escape_success()
                else:
                    print("Pas possible. C'est un mur!\n")
        elif direction == "bas":
            if labyrinth_structure[self.y_position + 1][self.x_position] == "O":
                self.y_position += 1
            else:
                if labyrinth_structure[self.y_position + 1][self.x_position] == "F":
                    self.escape_success()
                else:
                    print("Pas possible. C'est un mur!\n")
        else:
            print("La commande n'est pas correcte. Veuillez réessayer.")

    def escape_success(self):
        print("Bravo!! MacGyver a pu s'échapper!")
        sys.exit()

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
        """ This method prints the labyrinth. """

        for line in self.structure:
            line = ''.join(line)
            print(line)

    def update_labyrinth_structure(self, character):
        """ This method updates the labyrinth according the movement of one character """

        self.structure[character.y_position][character.x_position] = character.face

        if character.direction is not None:
            if character.direction == "droite":
                self.structure[character.y_position][character.x_position - 1] = "O"
            elif character.direction == "gauche":
                self.structure[character.y_position][character.x_position + 1] = "O"
            elif character.direction == "haut":
                self.structure[character.y_position + 1][character.x_position] = "O"
            elif character.direction == "bas":
                self.structure[character.y_position - 1][character.x_position] = "O"


def main():
    """ main function of the program """
    # Welcome message
    print("\n##########")
    print("Aide MacGyver à s'échapper du labyrinthe!")
    print("##########\n")

    # Initialization of the labyrinth
    labyrinth = Level('labyrinthe.json', 'line')
    labyrinth.generate_labyrinth_from_json()

    # Character Initialization + Labyrinth's structure update
    macgyver = Character(1, 1, 'X')
    labyrinth.update_labyrinth_structure(macgyver)
    gardien = Character(14, 12, 'F')
    labyrinth.update_labyrinth_structure(gardien)

    # Print labyrinth with Mac Gyver on its initial position
    labyrinth.print_labyrinth_into_terminal()

    # Start game
    while True:
        print("\n ----------")
        direction = input("Dans quel direction souhaites-tu diriger MacGyver?\n Tape droite pour aller à droite \n Tape gauche pour aller à gauche \n Tape haut pour aller en haut \n Tape bas pour aller en bas \n Ton choix : ")
        direction = direction.lower()
        print("----------\n")
        print("La direction que tu as choisie: {}\n".format(direction))

        macgyver.move(direction, labyrinth.structure)
        labyrinth.update_labyrinth_structure(macgyver)
        labyrinth.print_labyrinth_into_terminal()

if __name__ == "__main__":
    main()
