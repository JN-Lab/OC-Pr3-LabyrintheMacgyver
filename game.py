#! /usr/bin/env python3
# coding: utf-8
import random

import pygame

from level import *
from character import *
from item import *

class Game:

    def __init__(self, window, level):
        self.window = window
        self.level = level
        self.screen_interaction = pygame.Surface((600, 600))

        self.labyrinth = Level(self.level, 'line')
        self.hero = Character("hero")
        self.bad_guy = Character("bad_guy")

        self.needle = Item("N")
        self.tube = Item("T")
        self.ether = Item("E")

        self.play_game = True

        self.__prepare()

    def __prepare(self):
        """ This method positions the characters and objects in the labyrinth structure """

        # Define Characters' position
        self.hero.x_index = 1
        self.hero.y_index = 1
        self.bad_guy.x_index = 14
        self.bad_guy.y_index = 12

        self.labyrinth.structure[self.hero.y_index][self.hero.x_index] = self.hero.stripe_face
        self.labyrinth.structure[self.bad_guy.y_index][self.bad_guy.x_index] = self.bad_guy.stripe_face

        # Define Objects' position
        self.__get_item_position(self.needle)
        self.labyrinth.structure[self.needle.y_index][self.needle.x_index] = self.needle.stripe_face

        self.__get_item_position(self.tube)
        self.labyrinth.structure[self.tube.y_index][self.tube.x_index] = self.tube.stripe_face

        self.__get_item_position(self.ether)
        self.labyrinth.structure[self.ether.y_index][self.ether.x_index] = self.ether.stripe_face

    def __get_item_position(self, item):
        """ This private method generates random position for the items of the game
        according valid location in labyrinth structure """
        valid_location = []
        for index_line, line in enumerate(self.labyrinth.structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == "O":
                    valid_location.append([index_line, index_stripe])

        winner_location = random.choice(valid_location)
        item.y_index = winner_location[0]
        item.x_index = winner_location[1]

    def __update_level_design(self, screen):
        """ This method updates the image of labyrinth zone according the labyrinth structure """

        zone = pygame.Surface((40, 40))

        num_line = 0
        for line in self.labyrinth.structure:
            num_stripe = 0
            for stripe in line:
                x_corner_top_left = num_stripe * 40
                y_corner_top_left = num_line * 40
                if stripe == self.labyrinth.wall_stripe_face:
                    zone.blit(self.labyrinth.wall_image, (0, 0))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.labyrinth.floor_stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.hero.stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    zone.blit(self.hero.image, (4, 0), (0, 0, 40, 40))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.bad_guy.stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    zone.blit(self.bad_guy.image, (4, 4), (0, 0, 40, 40))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.needle.stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    zone.blit(self.needle.object_image, (4, 4))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.tube.stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    zone.blit(self.tube.object_image, (4, 4))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == self.ether.stripe_face:
                    zone.blit(self.labyrinth.floor_image, (0, 0))
                    zone.blit(self.labyrinth.floor_image, (0, 20))
                    zone.blit(self.ether.object_image, (4, 4))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                num_stripe += 1
            num_line += 1

    def update_screen(self):
        """ This method updates the labyrinth screens """

        self.window.blit(self.screen_interaction, (100, 100))
        self.__update_level_design(self.screen_interaction)
