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
        """ This private method selects the equipements to load from
        equipment-32x32.png """
        num_item = 0

        if self.stripe_face != ETHER_STRIPE:
            if self.stripe_face == NEEDLE_STRIPE:
                num_item = 12
            elif self.stripe_face == TUBE_STRIPE:
                num_item = 64

            item_images = pygame.image.load(EQUIPMENT_IMAGES).convert_alpha()

        elif self.stripe_face == ETHER_STRIPE:
            num_item = 6
            item_images = pygame.image.load(EXTRAS_IMAGES).convert_alpha()

        x_dim = 32
        y_dim = 32
        x_corner = num_item * x_dim - x_dim
        y_corner = 0
        object_image = item_images.subsurface((x_corner, y_corner, x_dim, y_dim))

        return object_image
