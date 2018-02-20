#! /usr/bin/env python3
# coding: utf-8

import random

class Object:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self):
        """ This method gives the attribute to the Object's item """
        self.x_index = 0
        self.y_index = 0
        self.image = self.get_image()

    def get_image(self):
        image_source = pygame.image.load("sources/equipement-32x32.png").convert_alpha()
        zone = pygame.Surface((40, 40))

        image = zone.blit(image_source, (4, 4), (0, 0, 40, 40))

        return image

    def get_position(self, labyrinth_structure):
        """ This method selects a random valid place in the labyrinth
         to get object position """
        valid_location = []
        for index_line, line in enumerate(labyrinth_structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == "O":
                    valid_location.append([index_line, index_stripe])
                else:
                    pass
        winner_location = random.choice(valid_location)
        self.y_index = winner_location[0]
        self.x_index = winner_location[1]
