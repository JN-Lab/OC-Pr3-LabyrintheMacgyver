#! /usr/bin/env python3
# coding: utf-8

import sys

import pygame

class Character:
    """ This class creates the characters for the game """

    def __init__(self, role):
        """ This method gives the different attributes to the character's object """
        self.x_index = 0
        self.y_index = 0
        self.role = role
        self.image = self.__get_image()
        self.stripe_face = self.__get_stripe_face()

        self.numb_items = 0
        self.direction = ""

    def __get_image(self):
        """ This method generates the image of the character according his role """

        if self.role == "hero":
            image = pygame.image.load("sources/macgyver-32x43.png").convert_alpha()
        else:
            image = pygame.image.load("sources/murdoc-32.png").convert_alpha()

        return image

    def __get_stripe_face(self):
        """ This method generate the stripe face of the character according his role """

        if self.role == "hero":
            stripe_face = "X"
        else:
            stripe_face = "F"

        return stripe_face

    def move(self, direction, labyrinth_structure):
        """ This method allows the character to move on the top, the right, the bottom
        or the left if there is no wall. At the same time, it manages the evolution
        of the structure according the movement of the main character. If the
        character reachs the F case, he wins. """

        self.direction = direction
        next_case_face = ""

        if direction == "droite":
            next_case_face = labyrinth_structure[self.y_index][self.x_index + 1]
            if next_case_face != "#":
                self.x_index += 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "gauche":
            next_case_face = labyrinth_structure[self.y_index][self.x_index - 1]
            if next_case_face != "#":
                self.x_index -= 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "haut":
            next_case_face = labyrinth_structure[self.y_index - 1][self.x_index]
            if next_case_face != "#":
                self.y_index -= 1
                if next_case_face != "O":
                    self.__touch(next_case_face)
            else:
                print("Pas possible. C'est un mur!\n")
        elif direction == "bas":
            next_case_face = labyrinth_structure[self.y_index + 1][self.x_index]
            if next_case_face != "#":
                self.y_index += 1
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
