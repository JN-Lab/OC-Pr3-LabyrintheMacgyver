#! /usr/bin/env python3
# coding: utf-8
import random

import pygame

from level import Level
from character import Character
from item import Item
from constants import *

class Game:
    """ This class manages the game """

    def __init__(self, level):
        self.window = self.__define_window()
        self.level = level
        self.screen_interaction = pygame.Surface((X_SCREEN_INTERACTION, Y_SCREEN_INTERACTION))

        self.labyrinth = Level(self.level)
        self.hero = Character("hero")
        self.bad_guy = Character("bad_guy")

        self.needle = Item(NEEDLE_STRIPE)
        self.tube = Item(TUBE_STRIPE)
        self.ether = Item(ETHER_STRIPE)

        self.selected_button = "play_game"
        self.play_button_color = WHITE
        self.quit_button_color = BLACK
        self.menu_message = "READY TO PLAY?"

        self.start_program = True
        self.menu = True
        self.play_game = False

    def __define_window(self):
        """ This method defines the window of the game """

        window = pygame.display.set_mode((X_WINDOW_GAME, Y_WINDOW_GAME))
        background = pygame.image.load("sources/background-jail-800x800.jpg").convert()
        window.blit(background, (0, 0))

        return window

    def __prepare(self):
        """ This method positions the characters and objects in the labyrinth structure """

        # Be sure to initialize all the characteristic of the game_over
        self.labyrinth = Level(self.level)
        self.hero = Character("hero")
        self.bad_guy = Character("bad_guy")

        self.needle = Item(NEEDLE_STRIPE)
        self.tube = Item(TUBE_STRIPE)
        self.ether = Item(ETHER_STRIPE)

        # Define Characters' position
        for index_line, line in enumerate(self.labyrinth.structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == HERO_STRIPE:
                    self.hero.x_index = index_stripe
                    self.hero.y_index = index_line
                elif stripe == BAD_GUY_STRIPE:
                    self.bad_guy.x_index = index_stripe
                    self.bad_guy.y_index = index_line

        # Define Objects' position
        random_positions = self.__get_item_positions(3)
        self.needle.x_index = random_positions[0][0]
        self.needle.y_index = random_positions[0][1]
        self.tube.x_index = random_positions[1][0]
        self.tube.y_index = random_positions[1][1]
        self.ether.x_index = random_positions[2][0]
        self.ether.y_index = random_positions[2][1]

        self.labyrinth.set_stripe(self.needle.x_index, self.needle.y_index, NEEDLE_STRIPE)
        self.labyrinth.set_stripe(self.tube.x_index, self.tube.y_index, TUBE_STRIPE)
        self.labyrinth.set_stripe(self.ether.x_index, self.ether.y_index, ETHER_STRIPE)

    def __get_item_positions(self, numb_position):
        valid_location = []
        for index_line, line in enumerate(self.labyrinth.structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == self.labyrinth.floor_stripe_face:
                    valid_location.append((index_stripe, index_line))

        winner_locations = random.sample(valid_location, numb_position)
        return winner_locations

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
        """ This method updates the console which contains the number of items
        collected by the Hero """

        console = pygame.Surface((600, 50))
        console.fill(BLACK)

        title_console = pygame.Surface((200, 50))
        font_text = pygame.font.SysFont('freesans', 36)
        item_text = font_text.render("Item Number: " + str(self.hero.numb_items), True, WHITE)

        title_console.blit(item_text, (0, 0))
        console.blit(title_console, (0, 12))

        self.__update_item_console(self.needle, self.hero, console)
        self.__update_item_console(self.tube, self.hero, console)
        self.__update_item_console(self.ether, self.hero, console)

        screen.blit(console, (0, 600))

    def __update_item_console(self, item, character, surface):
        numb_items = character.get_numb_items()
        x_console = 0
        if item.found:
            item_console = pygame.Surface((50, 50))
            item_console.blit(self.needle.object_image, (9, 9))
            if numb_items == 1:
                x_console = 200
            elif numb_items == 2:
                x_console = 250
            elif numb_items == 3:
                x_console = 300
            surface.blit(item_console, (x_console, 0))

    def __update_menu_design(self, screen):
        """ This method updates the menu selection """

        # Get the fonts
        choice_text = pygame.font.SysFont('freesans', 50)

        # Creation of game statut
        game_statut = pygame.Surface((X_MESSAGE, Y_MESSAGE))
        game_statut.fill(DARKGRAY)
        text_statut = choice_text.render(self.menu_message, True, WHITE)
        text_statut_position = text_statut.get_rect()
        text_statut_position.centerx = game_statut.get_rect().centerx
        text_statut_position.centery = game_statut.get_rect().centery
        game_statut.blit(text_statut, text_statut_position)

        # Creation of play button
        play_button = pygame.Surface((X_BUTTON, Y_BUTTON))
        play_button.fill(DARKGRAY)
        pygame.draw.rect(play_button, self.play_button_color, (0, 0, X_BUTTON, Y_BUTTON), BORDER)
        play_text = choice_text.render("PLAY", True, self.play_button_color)
        play_text_position = play_text.get_rect()
        play_text_position.centerx = play_button.get_rect().centerx
        play_text_position.centery = play_button.get_rect().centery
        play_button.blit(play_text, play_text_position)

        # Creation of quit button
        quit_button = pygame.Surface((X_BUTTON, Y_BUTTON))
        quit_button.fill(DARKGRAY)
        pygame.draw.rect(quit_button, self.quit_button_color, (0, 0, X_BUTTON, Y_BUTTON), BORDER)
        quit_text = choice_text.render("QUIT", True, self.quit_button_color)
        quit_text_position = quit_text.get_rect()
        quit_text_position.centerx = quit_button.get_rect().centerx
        quit_text_position.centery = quit_button.get_rect().centery
        quit_button.blit(quit_text, quit_text_position)

        # Integration of the different elements into screen
        screen.blit(game_statut, (20, 0))
        screen.blit(play_button, (150, 300))
        screen.blit(quit_button, (150, 425))

    def __update_screen_interaction(self):
        """ This method updates the labyrinth screens """
        self.screen_interaction.fill(DARKGRAY)
        if self.menu:
            self.__update_menu_design(self.screen_interaction)
        elif self.play_game:
            self.__update_level_design(self.screen_interaction)
            self.__update_level_console(self.screen_interaction)

        self.window.blit(self.screen_interaction, (X_CORNER_SCREEN_INTERACTION, Y_CORNER_SCREEN_INTERACTION))

    def __process_event_menu(self, event: pygame.event):
        """ This method groups all the interaction the player can have with the menu """

        self.__interact_with_button_menu(event)
        self.__select_option_menu(event)

    def __interact_with_button_menu(self, event: pygame.event):
        """ This method manages the switch between menu button """

        if self.selected_button == "play_game" and event.key == pygame.K_DOWN:
            self.play_button_color = BLACK
            self.quit_button_color = WHITE
            self.selected_button = "quit_game"
        elif self.selected_button == "quit_game" and event.key == pygame.K_UP:
            self.play_button_color = WHITE
            self.quit_button_color = BLACK
            self.selected_button = "play_game"

    def __select_option_menu(self, event: pygame.event):
        """ This method manages the menu button selection """

        if self.selected_button == "play_game" and event.key == pygame.K_RETURN:
            self.menu = False
            self.play_game = True
            self.__prepare()
        elif self.selected_button == "quit_game" and event.key == pygame.K_RETURN:
            self.start_program = False

    def __process_event_game(self, event: pygame.event):
        """ This method manages the process of the game"""

        if event.key == pygame.K_RIGHT:
            self.hero.move("right", self.labyrinth)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_LEFT:
            self.hero.move("left", self.labyrinth)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_UP:
            self.hero.move("up", self.labyrinth)
            self.labyrinth.update_labyrint_structure(self.hero)
        elif event.key == pygame.K_DOWN:
            self.hero.move("down", self.labyrinth)
            self.labyrinth.update_labyrint_structure(self.hero)

    def __get_status_game(self, event: pygame.event):
        """ this method will determine the statut of the game when Mac Gyver
        will touch Murdoc """

        game_status = ""
        if event.key == pygame.K_RIGHT:
            game_status = self.hero.touch_something("right", self.labyrinth)
        elif event.key == pygame.K_LEFT:
            game_status = self.hero.touch_something("left", self.labyrinth)
        elif event.key == pygame.K_UP:
            game_status = self.hero.touch_something("up", self.labyrinth)
        elif event.key == pygame.K_DOWN:
            game_status = self.hero.touch_something("down", self.labyrinth)

        if game_status == "game_over":
            self.play_game = False
            self.menu = True
            self.menu_message = "GAME OVER - ANOTHER ONE?"
        elif game_status == "win":
            self.play_game = False
            self.menu = True
            self.menu_message = "WINNER - ANOTHER ONE?"
        elif game_status == "found_needle":
            self.needle.found = True
        elif game_status == "found_ether":
            self.ether.found = True
        elif game_status == "found_tube":
            self.tube.found = True

    def start(self):
        """ This method loads the game """

        while self.start_program:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start_program = False
                elif event.type == pygame.KEYDOWN:
                    if self.menu:
                        self.__process_event_menu(event)
                    elif self.play_game:
                        self.__get_status_game(event)
                        self.__process_event_game(event)
                    else:
                        self.start_program = False
            self.__update_screen_interaction()
            pygame.display.flip()
