#! /usr/bin/env python3
# coding: utf-8

import random

class Object:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self, face):
        """ This method gives the attribute to the Object's item """
        self.x_position = 0
        self.y_position = 0
        self.face = face
        self.direction = ""

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
        self.y_position = winner_location[0]
        self.x_position = winner_location[1]
