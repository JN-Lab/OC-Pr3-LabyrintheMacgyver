#! /usr/bin/env python3
# coding: utf-8

import random

import pygame

from constants import *

class Item:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self, stripe_face):
        """ This method gives the attribute to the Object's item """
        self.x_index = 0
        self.y_index = 0
        self.stripe_face = stripe_face
        self.object_image = self.__get_image()
        self.found = False

    def __get_image(self):
        """ This private method selects the equipements to load from equipment-32x32.png """
        num_item = 0

        if self.stripe_face != ETHER_STRIPE:
            if self.stripe_face == NEEDLE_STRIPE:
                num_item = 12
            elif self.stripe_face == TUBE_STRIPE:
                num_item = 64

            object_selection_images = pygame.image.load(EQUIPMENT_IMAGES).convert_alpha()

        elif self.stripe_face == ETHER_STRIPE:
            num_item = 6
            object_selection_images = pygame.image.load(EXTRAS_IMAGES).convert_alpha()

        x_dim_image = 32
        y_dim_image = 32
        x_corner_image = num_item * x_dim_image - x_dim_image
        y_corner_image = 0
        object_image = object_selection_images.subsurface((x_corner_image, y_corner_image, x_dim_image, y_dim_image))

        return object_image
