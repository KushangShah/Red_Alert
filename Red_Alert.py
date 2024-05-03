# Import libraries
import pygame
import pyzero
import pgzero
import pgzrun
import random

# define screen ratio
WIDTH = 1000
HEIGHT = 600

# Find center of screen
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)

# set font colour
FONT_COLOR = (255, 255, 255)

# Initialize speed
START_SPEED = 10

# select start which should not be clicked
COLOR = ['Bluw_star', 'green_start']

# Set Finial Level
FINAL_LEVEL = 6

"""
Constants are variables whose value shouldn’t change after they are first set. 
Programmers use capital letters when naming them to let other programmers know not 
to change their values. This is known as a “naming convention”—a rule that most 
programmers agree on, so that everyone’s code looks similar and is easier to understand.
"""

# pgzrun /Users/bina/Code?/Exercise/Game?/Red_Alert/Red_Alert.py

# Defining some global variables
game_over = False
game_complete = False
current_level = 0
stars = []
animation = []

# Doing the animation part
def draw():
    global stars, current_level, game_over, game_complete 
    screen.clear()
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "Try again.") 
    elif game_complete:
        display_message("YOU WON!", "Well done.") 
    else:
        for star in stars:
            star.draw()
# Make Star
def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

# Defining make_stars
def make_stars(number_of_extra_stars):
    colour_to_create = get_colour_to_create(number_of_extra_stars)  # This retur list of start that will be put in display
    new_stars = create_stars(colour_to_create)  # This function uses the list of colors as a parameter and creates Actors for each star.
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colour_to_create(number_of_extra_stars):
    []

def create_stars(colour_to_create):
    []

def layout_stars(stars_to_layout):
    pass

def animate_stars(stars_to_animate):
    pass


