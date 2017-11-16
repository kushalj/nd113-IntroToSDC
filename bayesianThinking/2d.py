""" 2d """

import numpy as np


# A simple robot world can be defined by a 2D array
# Here is a 6x5 (num_rows x num_cols) world
world = np.array([ [0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0] ])

# Visualize the world
print(world)

# Print out some information about the world

print('The shape of this array is: ' + str(world.shape))
print('Notice that the x and y dimensions are in the opposite order than usual!')
print('It\'s height is: ' + str(world.shape[1]) +
      ', and it\'s length/width is: ' + str(world.shape[0]))


# Access a location and read its value
value = world[3][0]
print('\n')
print('Value at index [3, 0] = ' +str(value))

# Read the first three items in the 3rd row
row = 2
column_index = 0
value_left = world[row, column_index]
value_middle = world[row, column_index + 1]
value_right = world[row, column_index + 2]

print('\nThe first three values in row 2 : ' +str(value_left)+', '
                                              +str(value_middle) +', '
                                              +str(value_right) )

# Compare the first two values and print the result
compare = world[0][0] == world[0][1]
print('\nDo the first two values match? ' + str(compare))


# Define a function to plant a tree
# and change the value of the array in that location
def plant_tree(y, x):
    # check that the indices are in the boundaries of the array dimensions
    if(y < world.shape[0] and x < world.shape[1]):
        world[y,x] = 1
        print('\n' + str(world)) # prints a newline and the current world

# Call the function at the location x = 3, and y = 2
# You can call this multiple times in a row
plant_tree(0, 2)



# A 6x5 robot world
world = np.array([ [0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0] ])

# Print out some information about the world
print(world)
print('\nThe shape of this array is: ' + str(world.shape))


def iterate2D(world):
    # y
    for i in range(0, world.shape[0]):
        # x
        for j in range(0, world.shape[1]):
            print('Index ['+str(i)+']['+str(j)+'] = '+str(world[i][j]))

print('\n')
iterate2D(world)


# This function is similar to our iterate2D function,
# But looks for the first tree in the array and prints its location [x][y]
def first_tree(world):
    # iterates through all indices starting at the top-left [0][0]
    for i in range(0, world.shape[0]):
        for j in range(0, world.shape[1]):
            # check if a tree is found
            if(world[i][j] == 1):
                # if so, print the index and leave the loop with a return statement
                print('First tree found at location: ['+str(i)+']['+str(j)+']')
                return


# Call the first_tree function
print('\n')
first_tree(world)
