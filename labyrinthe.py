#! /usr/bin/env python3
# coding: utf-8

import pygame

from game import *
from constants import *

def main():
    pygame.init()

    game = Game("labyrinthe.json")
    game.start()

    pygame.quit()


if __name__ == "__main__":
    main()
