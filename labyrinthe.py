#! /usr/bin/env python3
# coding: utf-8

import pygame

from game import *
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((X_WINDOW_GAME, Y_WINDOW_GAME))
    background = pygame.image.load("sources/background-jail-800x800.jpg").convert()
    window.blit(background, (0, 0))

    play = 1
    game = Game(window, "labyrinthe.json")

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = 0
            elif event.type == pygame.KEYDOWN:
                game.start(event)

        game.update_screen_interaction()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
