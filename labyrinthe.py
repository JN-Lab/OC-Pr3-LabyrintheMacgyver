#! /usr/bin/env python3
# coding: utf-8

import pygame

from game import *

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 800))

    game = Game(window, "labyrinthe.json")

    play = 1
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = 0

        game.update_screen()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
