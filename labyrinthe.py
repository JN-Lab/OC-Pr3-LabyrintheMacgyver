import os

def print_labyrinthe(data_file):
    """ This is the main function of the file """
    directory = os.path.dirname(__file__) # We get the right path
    path_to_file = os.path.join(directory, 'sources', data_file) # We build the path

    with open(path_to_file, "r") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    print_labyrinthe('labyrinthe.txt')
