""" Different constants of the game """

# String to identify each character in level structure
HERO_STRIPE = "X"
BAD_GUY_STRIPE = "F"
ETHER_STRIPE = "E"
TUBE_STRIPE = "T"
NEEDLE_STRIPE = "N"
WALL_STRIPE = "#"
FLOOR_STRIPE = "O"

# Path for the different sources of the game
HERO_IMAGE = "sources/macgyver-32x43.png"
BAD_GUY_IMAGE = "sources/murdoc-32.png"
EQUIPMENT_IMAGES = "sources/equipment-32x32.png"
EXTRAS_IMAGES = "sources/extras-32x32.png"
WALL_IMAGES = "sources/wall-tiles-40x40.png"
FLOOR_IMAGES = "sources/floor-tiles-20x20.png"

# Different Dimension linked of surface of the Game
X_WINDOW_GAME = 800
Y_WINDOW_GAME = 800
X_SCREEN_INTERACTION = 600
Y_SCREEN_INTERACTION = 650
X_CORNER_SCREEN_INTERACTION = (X_WINDOW_GAME - X_SCREEN_INTERACTION) / 2
Y_CORNER_SCREEN_INTERACTION = (Y_WINDOW_GAME - Y_SCREEN_INTERACTION) / 2
X_LEVEL_DIM_CASE = 40
Y_LEVEL_DIM_CASE = 40
X_MESSAGE = 600
Y_MESSAGE = 80
X_BUTTON = X_SCREEN_INTERACTION / 2
Y_BUTTON = 80
BORDER = 2

# Color
WHITE = 255, 255, 255
BLACK = 0, 0, 0
BLUE = 0, 0, 99
DARKGRAY = 40, 40, 40
