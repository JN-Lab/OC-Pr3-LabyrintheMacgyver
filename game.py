#! /usr/bin/env python3
# coding: utf-8
import random

import pygame

from level import *
from character import *
from item import *
from constants import *

class Game:

    def __init__(self, window, level):
        self.window = window
        self.level = level
        self.screen_interaction = pygame.Surface((X_SCREEN_INTERACTION, Y_SCREEN_INTERACTION))

        self.labyrinth = Level(self.level, 'line')
        self.hero = Character("hero")
        self.bad_guy = Character("bad_guy")

        self.needle = Item(NEEDLE_STRIPE)
        self.tube = Item(TUBE_STRIPE)
        self.ether = Item(ETHER_STRIPE)

        self.menu = False
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
                if stripe == self.labyrinth.floor_stripe_face:
                    valid_location.append([index_line, index_stripe])

        winner_location = random.choice(valid_location)
        item.y_index = winner_location[0]
        item.x_index = winner_location[1]

    def __update_level_design(self, screen):
        """ This method updates the image of labyrinth labyrinth_case according the labyrinth structure """

        labyrinth_case = pygame.Surface((X_LEVEL_DIM_CASE, Y_LEVEL_DIM_CASE))

        num_line = 0
        for line in self.labyrinth.structure:
            num_stripe = 0
            for stripe in line:
                x_corner_top_left = num_stripe * X_LEVEL_DIM_CASE
                y_corner_top_left = num_line * Y_LEVEL_DIM_CASE
                if stripe == WALL_STRIPE:
                    labyrinth_case.blit(self.labyrinth.wall_image, (0, 0))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == FLOOR_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == HERO_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    labyrinth_case.blit(self.hero.image, (4, 0), (0, 0, X_LEVEL_DIM_CASE, Y_LEVEL_DIM_CASE))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == BAD_GUY_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    labyrinth_case.blit(self.bad_guy.image, (4, 4), (0, 0, X_LEVEL_DIM_CASE, Y_LEVEL_DIM_CASE))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == NEEDLE_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    labyrinth_case.blit(self.needle.object_image, (4, 4))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == TUBE_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    labyrinth_case.blit(self.tube.object_image, (4, 4))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                elif stripe == ETHER_STRIPE:
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 0))
                    labyrinth_case.blit(self.labyrinth.floor_image, (0, 20))
                    labyrinth_case.blit(self.ether.object_image, (4, 4))
                    screen.blit(labyrinth_case, (x_corner_top_left, y_corner_top_left))
                num_stripe += 1
            num_line += 1

    def __update_level_console(self, screen):
        """ This method updates the console which contains the number of items collected by the Hero """
        console = pygame.Surface((600, 100))
        pygame.draw.rect(console, (180, 20, 150), (0, 0, 600, 50))
        screen.blit(console, (0, 600))

    def update_interaction_screen(self):
        """ This method updates the labyrinth screens """

        self.window.blit(self.screen_interaction, (X_CORNER_SCREEN_INTERACTION, Y_CORNER_SCREEN_INTERACTION))
        self.__update_level_design(self.screen_interaction)
        self.__update_level_console(self.screen_interaction)

    def __update_menu_design(self, screen):
        pass

    def __process_event_game(self, event: pygame.event):
        if event.key == pygame.K_RIGHT:
            self.hero.move("right", self.labyrinth.structure)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_LEFT:
            self.hero.move("left", self.labyrinth.structure)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_UP:
            self.hero.move("up", self.labyrinth.structure)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_DOWN:
            self.hero.move("down", self.labyrinth.structure)
            self.labyrinth.update_labyrint_structure(self.hero)

    def start(self, event: pygame.event):
        """ This method loads the game """
        if self.menu:
            pass
        elif self.play_game:
            self.__process_event_game(event)
