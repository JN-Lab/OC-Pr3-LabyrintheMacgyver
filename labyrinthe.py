import os
import json

class Level:
    """ This class loads the structure of the labyrinth """

    def __init__(self, data_file, key):
        self.data_file = data_file
        self.key = key
        self.structure = []

    def generate_labyrinth_from_json(self):
        """ This function loads the labyrinth's structure into a list
        containing each line. Each line is a list containing each stripe.
        example : structure = [[stripe1_from_line1, stripe2_from_line1,...],
        [stripe1_from_line2, stripe2_from_line2,...],...] """

        labyrinth_structure = []

        directory = os.path.dirname(__file__) # We get the right path
        path_to_file = os.path.join(directory, 'sources', self.data_file) # We build the path

        with open(path_to_file, "r") as file:
            data = json.load(file)
            for lines in data:
                labyrinth_lines = []
                for stripe in lines[self.key]:
                    labyrinth_lines.append(stripe)
                labyrinth_structure.append(labyrinth_lines)

        self.structure = labyrinth_structure

    def print_labyrinth_into_terminal(self):
        """ This function print the labyrinth into the terminal """

        for line in self.structure:
            line = ''.join(line)
            print(line)

def main():
    labyrinth = Level('labyrinthe.json', 'line')
    labyrinth.generate_labyrinth_from_json()
    labyrinth.print_labyrinth_into_terminal()

if __name__ == "__main__":
    main()
