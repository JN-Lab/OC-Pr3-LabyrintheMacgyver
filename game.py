#! /usr/bin/env python3
# coding: utf-8

import pygame

from level import *

class Game:

    def __init__(self, window, screen_play, level):
        self.window = window
        self.level = level
        self.screen_play = screen_play

        self.labyrinth = Level(self.level, 'line')

        self.play_game = True


    def prepare(self):
        """ This methd resets the game if needed """
        self.play_game = True
        self.labyrinth = Level(self.level, 'line')

    def start(self):

        self.window.blit(self.screen_play, (200, 200))
        self.labyrinth.print_level(self.screen_play)
