import os
import json

def read_labyrinth_from_json(data_file, key):
    """ This function loads the labyrinth's structure into a list
    containing each line. Each line is a list containing each stripe.
    example : structure = [[stripe1_from_line1, stripe2_from_line1,...],
     [stripe1_from_line2, stripe2_from_line2,...],...] """

    labyrinth_structure = []

    directory = os.path.dirname(__file__) # We get the right path
    path_to_file = os.path.join(directory, 'sources', data_file) # We build the path

    with open(path_to_file, "r") as file:
        data = json.load(file)
        for lines in data:
            labyrinth_lines = []
            for stripe in lines[key]:
                labyrinth_lines.append(stripe)
            labyrinth_structure.append(labyrinth_lines)

    return labyrinth_structure

def print_labyrinth(lines):
    """ This function print the labyrinth into the terminal """

    for line in lines:
        line = ''.join(line)
        print(line)

if __name__ == "__main__":
    structure = read_labyrinth_from_json('labyrinthe.json', 'line')
    print_labyrinth(structure)
