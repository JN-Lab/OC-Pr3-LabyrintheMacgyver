#! /usr/bin/env python3
# coding: utf-8

import pygame

from game import *
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((X_WINDOW_GAME, Y_WINDOW_GAME))
    background = pygame.image.load("sources/background-jail-800x800.jpg").convert()

    game = Game(window, "labyrinthe.json")

    play = 1
    while play:
        window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.hero.move("droite", game.labyrinth.structure)
                    game.labyrinth.update_labyrint_structure(game.hero)
                    print("a droite")
                    print(game.hero.x_index)
                elif event.key == pygame.K_LEFT:
                    game.hero.move("gauche", game.labyrinth.structure)
                    game.labyrinth.update_labyrint_structure(game.hero)
                    print("a droite")
                elif event.key == pygame.K_UP:
                    game.hero.move("haut", game.labyrinth.structure)
                    game.labyrinth.update_labyrint_structure(game.hero)
                    print("a droite")
                elif event.key == pygame.K_DOWN:
                    game.hero.move("bas", game.labyrinth.structure)
                    game.labyrinth.update_labyrint_structure(game.hero)
                    print("a droite")
                print(game.labyrinth.structure)
        game.update_level_screen()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
