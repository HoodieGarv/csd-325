"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation

MODIFICATION LOG (Module 6):
- Added WATER constant ('~') to represent lake tiles.
- Added lake generation in createNewForest() using an ellipse formula
  centered at (WIDTH // 2, HEIGHT // 2) with semi-axes a=10, b=4.
  Terminal characters are taller than wide, so a wider x-axis produces
  a visually round shape.
- Added WATER rendering in displayForest() using bext blue foreground.
- Water tiles are permanent: the simulation loop's existing else-branch
  copies any unrecognized state (including WATER) unchanged each tick.
  Fire spread only targets cells equal to TREE, so WATER is never
  overwritten by the neighbor-ignition logic. No additional guard is
  required beyond placing WATER in the initial forest.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
# MODIFICATION: New constant for the water/lake tile.
# '~' visually suggests water and is distinct from TREE ('A') and FIRE ('@').
WATER = '~'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees.
                            # MODIFICATION NOTE: WATER cells are never TREE,
                            # so this check naturally prevents fire from
                            # crossing the lake. No explicit WATER guard needed.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object.
                    # MODIFICATION NOTE: WATER cells fall through to this branch
                    # every tick, preserving them unchanged for the lifetime of
                    # the simulation.
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # MODIFICATION: Define the lake as an ellipse centered on the display.
    # Center coordinates:
    cx = WIDTH // 2   # x-center = 39
    cy = HEIGHT // 2  # y-center = 11
    # Semi-axes: wider on x because terminal characters are taller than wide,
    # which makes equal pixel radii look oval. a=10, b=4 produces a roughly
    # circular visual shape.
    a = 10  # horizontal semi-axis (columns)
    b = 4   # vertical semi-axis (rows)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Check whether this cell falls inside the lake ellipse.
            # Ellipse formula: (x-cx)^2/a^2 + (y-cy)^2/b^2 <= 1
            if ((x - cx) ** 2 / a ** 2) + ((y - cy) ** 2 / b ** 2) <= 1:
                forest[(x, y)] = WATER  # Place permanent lake tile.
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE   # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            # MODIFICATION: Render water tiles in blue.
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
