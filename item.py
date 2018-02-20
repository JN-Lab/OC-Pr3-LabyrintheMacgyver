#! /usr/bin/env python3
# coding: utf-8

import random

import pygame

class Item:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self, stripe_face):
        """ This method gives the attribute to the Object's item """
        self.x_index = 0
        self.y_index = 0
        self.stripe_face = stripe_face
        self.object_image = self.__get_image()

    def __get_image(self):
        """ This private method selects the equipements to load from equipment-32x32.png """
        object_selection_images = pygame.image.load("sources/equipment-32x32.png").convert_alpha()
        object_image = object_selection_images.subsurface((0, 0, 32, 32))

        return object_image
