#! /usr/bin/env python3
# coding: utf-8

import pygame

from level import *
from character import *

class Game:

    def __init__(self, window, level):
        self.window = window
        self.level = level
        self.screen_interaction = pygame.Surface((600, 600))

        self.labyrinth = Level(self.level, 'line')
        self.hero = Character("hero")
        self.bad_guy = Character("bad_guy")

        self.play_game = True

        self.__prepare()

    def __prepare(self):
        """ Thie method positions the characters and objects in the labyrinth structure """

        self.hero.x_index = 1
        self.hero.y_index = 1
        self.bad_guy.x_index = 14
        self.bad_guy.y_index = 12

        self.labyrinth.structure[self.hero.y_index][self.hero.x_index] = self.hero.stripe_face
        self.labyrinth.structure[self.bad_guy.y_index][self.bad_guy.x_index] = self.bad_guy.stripe_face

    def __update_level_design(self, screen):
        # Lire la structure du niveau
        # En fonction des stripes du niveau, j'y assigne les bonnes zones
        zone = pygame.Surface((40, 40))

        num_line = 0
        for line in self.labyrinth.structure:
            num_stripe = 0
            for stripe in line:
                x_corner_top_left = num_stripe * 40
                y_corner_top_left = num_line * 40
                if stripe == "#":
                    zone.blit(self.labyrinth.wall_images, (0, 0), (300, 20, 40, 40))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == "O":
                    zone.blit(self.labyrinth.floor_images, (0, 0), (240, 120, 40, 20))
                    zone.blit(self.labyrinth.floor_images, (0, 20), (240, 120, 40, 20))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == "X":
                    zone.blit(self.labyrinth.floor_images, (0, 0), (240, 120, 40, 20))
                    zone.blit(self.labyrinth.floor_images, (0, 20), (240, 120, 40, 20))
                    zone.blit(self.hero.image, (4, 0), (0, 0, 40, 40))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                elif stripe == "F":
                    zone.blit(self.labyrinth.floor_images, (0, 0), (240, 120, 40, 20))
                    zone.blit(self.labyrinth.floor_images, (0, 20), (240, 120, 40, 20))
                    zone.blit(self.bad_guy.image, (4, 4), (0, 0, 40, 40))
                    screen.blit(zone, (x_corner_top_left, y_corner_top_left))
                num_stripe += 1
            num_line += 1

    def update_screen(self):

        self.window.blit(self.screen_interaction, (100, 100))
        self.__update_level_design(self.screen_interaction)
