import os
import json

def read_labyrinth_from_json(data_file, key):
    """ This is the main function of the file """
    lines_from_labyrinth = []

    directory = os.path.dirname(__file__) # We get the right path
    path_to_file = os.path.join(directory, 'sources', data_file) # We build the path

    with open(path_to_file, "r") as file:
        data = json.load(file)
        for entry in data:
            lines_from_labyrinth.append(entry[key])

    return lines_from_labyrinth

def print_labyrinth(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    lines = read_labyrinth_from_json('labyrinthe.json', 'line')
    print_labyrinth(lines)
