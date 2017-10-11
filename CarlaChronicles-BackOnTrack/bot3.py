""" Back on Track exercises """
from mymath import TAU

# a_lat max = 12 m/s^2
# v = 30 m/s

def a_lat(v, r):
    return v**2/r

v = 30
for r in [50, 31.4, 75, 16]:
    print("a_lat for radius {0}: {1}".format( r, a_lat(v, r) ))
