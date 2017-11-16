""" roadArray.py """

import numpy as np


# the roadArray
road = np.array(['r', 'r', 'r', 'r', 'r', 's','r'])

print('The length of this array is: ' +str(len(road)))

value = road[0]
print('\n')
print('Value at index [0] = ' +str(value))

value_end = road[-1]
print('\n')
print('Value at index [-1] = ' +str(value_end))

equal = (value == value_end)
print('\n')
print('Are the first and last values equal? ' +str(equal))

length = len(road)
for index in range(0, length):
    value = road[index]
    print('road['+str(index)+'] = '+str(value))

for index in range(0, length):
    print(str(index))
    if index == 3:
        print('We\'ve reached the middle of the loop and we\'re leaving the loop')
        break

length = len(road)
def find_stop_index(road):
    stop_index = 0
    for index in range(0, length):
        if index+1 < length and road[index+1] == 's':
            stop_index = index

    return stop_index
