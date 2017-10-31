""" pattern matching """

import numpy as np

# A 4x5 robot world of characters 'o' and 'b'
world = np.array([ ['o', 'b', 'o', 'o', 'b'],
                   ['o', 'o', 'b', 'o', 'o'],
                   ['b', 'o', 'o', 'b', 'o'],
                   ['b', 'o', 'o', 'o', 'o'] ])

# Sensor measurement
measurement = ['b', 'o']

# This function takes in the world and the sensor measurement.
# Complete this function so that it returns the indices of the
# likely robot locations, based on matching the measurement
# with the color patterns in the world

def find_match(world, measurement):
    # Empty possible_locations list
    possible_locations = []

    ## TODO: Iterate through the world
    ## Look at two adjacent indices at a time - the square the robot is
    ## on top of and the square to its right
    ## (Making sure not to go past the bounds of the world)

    ## TODO: If two adjacent colors in the world match
    ## the two colors in the sensor measurement
    ## Add those indices to the possible_locations list
    ## Append them in the format [row_index, column_index], i.e. [0, 0]

    for y_pos in range(0, world.shape[0]):
        for x_pos in range(0, world.shape[1]):
            # compare y,x with measurement char
            if measurement[0] == world[y_pos][x_pos]:
                # check we don't run over the end of the row
                if x_pos+1 < world.shape[1]:
                    # does square to the right match world square to the right?
                    if measurement[1] == world[y_pos][x_pos+1]:
                        possible_locations.append([y_pos, x_pos])


    return possible_locations


# This line runs the function and stores the output - do not delete
locations = find_match(world, measurement)
print(locations)
