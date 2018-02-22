#! /usr/bin/env python3
# coding: utf-8
import random

import pygame

from level import *
from character import *
from item import *
from constants import *

class Game:

    def __init__(self, level):
        self.window = self.__define_window()
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

    def __define_window(self):
        window = pygame.display.set_mode((X_WINDOW_GAME, Y_WINDOW_GAME))
        background = pygame.image.load("sources/background-jail-800x800.jpg").convert()
        window.blit(background, (0, 0))

        return window

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
        console = pygame.Surface((600, 50))
        console.fill(BLACK)

        title_console = pygame.Surface((200, 50))
        font_text = pygame.font.SysFont('freesans', 36)
        item_text = font_text.render("Item Number: " + str(self.hero.numb_items), True, WHITE)

        title_console.blit(item_text, (0, 0))
        console.blit(title_console, (0, 12))
        screen.blit(console, (0, 600))

    def __update_menu_design(self, screen):
        """ This method updates the menu selection """
        # Get the fonts
        choice_text = pygame.font.SysFont('freesans', 50)

        # Creation of game statut
        game_statut = pygame.Surface((600, 80))
        game_statut.fill(DARKGRAY)
        text_statut = choice_text.render("PRET A JOUER?", True, WHITE)
        text_statut_position = text_statut.get_rect()
        text_statut_position.centerx = game_statut.get_rect().centerx
        text_statut_position.centery = game_statut.get_rect().centery
        game_statut.blit(text_statut, text_statut_position)

        # Creation of play button
        play_button = pygame.Surface((300, 80))
        play_button.fill(DARKGRAY)
        pygame.draw.rect(play_button, WHITE, (0, 0, 300, 80), 2)
        play_text = choice_text.render("PLAY", True, WHITE)
        play_text_position = play_text.get_rect()
        play_text_position.centerx = play_button.get_rect().centerx
        play_text_position.centery = play_button.get_rect().centery
        play_button.blit(play_text, play_text_position)

        # Creation of quit button
        quit_button = pygame.Surface((300, 80))
        quit_button.fill(DARKGRAY)
        pygame.draw.rect(quit_button, WHITE, (0, 0, 300, 80), 2)
        quit_text = choice_text.render("QUIT", True, WHITE)
        quit_text_position = quit_text.get_rect()
        quit_text_position.centerx = quit_button.get_rect().centerx
        quit_text_position.centery = quit_button.get_rect().centery
        quit_button.blit(quit_text, quit_text_position)

        # Integration of the different elements into screen
        screen.blit(game_statut, (10, 0))
        screen.blit(play_button, (150, 300))
        screen.blit(quit_button, (150, 425))

    def update_screen_interaction(self):
        """ This method updates the labyrinth screens """
        self.screen_interaction.fill(DARKGRAY)
        if self.menu:
            self.__update_menu_design(self.screen_interaction)
        elif self.play_game:
            self.__update_level_design(self.screen_interaction)
            self.__update_level_console(self.screen_interaction)

        self.window.blit(self.screen_interaction, (X_CORNER_SCREEN_INTERACTION, Y_CORNER_SCREEN_INTERACTION))

    def __process_event_menu(self, event: pygame.event):
        pass

    #def __update_button_menu_design(self, selected_button):
        #selected_button = play_game
        #if selected_button == play_game:
            #bouton play_game = texte blanc et contour blanc
            #bouton quit_game = texte noir et contour noir
        #elif selected_button == quit_game:
            #bouton play_game = texte noir et contour noir
            #bouton quit_game = texte blanc et contour blanc

    #def __interact_with_button_menu(self, selected_button):
        #if selected_button == play_game and event.key == pygame.K_DOWN:
            #selected_button = quit_game
        #elif selected_button == quit_game and event.key == pyagme.K_UP:
            #selected_button = play_game

    #def __select_option_menu(self, selected_button):
        #if selected_button == play_game and event.key == pygame.K_KP_ENTER:
            #self.menu = False
            #self.play_game = True
        #elif selected_button == quit_game and event.key == pygame.K_KP_ENTER:
            #self.menu = False
            #self.play_game = False
        pass


    def __process_event_game(self, event: pygame.event):
        """ This method manages the process of the game """
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

    def __process_end_game(self, event: pygame.event):
        """ this method will determine the statut of the game when Mac Gyver will touch Murdoc """
        # Si 3 items -> Bravo sinon -> Looser
        # self.play_game = False
        # self.menu = True
        pass

    def start(self):
        """ This method loads the game """
        start_program = 1

        while start_program:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_program = 0
                elif event.type == pygame.KEYDOWN:
                    if self.menu:
                        pass
                        #self.__process_event_menu(event)
                        #return 1
                    elif self.play_game:
                        self.__process_event_game(event)
                        #self.__process_end_game(event)
                        #return 1
                    #else:
                        #return 0
            self.update_screen_interaction()
            pygame.display.flip()
