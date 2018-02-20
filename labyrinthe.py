#! /usr/bin/env python3
# coding: utf-8

import pygame

from game import *

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))

    screen_play = pygame.Surface((600, 600))
    #labyrinth = Level("labyrinthe.json", "line")

    game = Game(window, screen_play, 'labyrinthe.json')

    play = 1
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = 0
        game.start()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
