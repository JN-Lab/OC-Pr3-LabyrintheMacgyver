#! /usr/bin/env python3
# coding: utf-8

import sys

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
