""" Back on Track exercises """
from mymath import TAU

def get_tire_diameter(dist_before_turn, dist_after_turn):
    circumference = dist_after_turn - dist_before_turn
    # diameter = circumference/pi
    diameter = 2 * (circumference / TAU)
    return diameter

print("Diameter: {0}".format( get_tire_diameter(1.0, 6.0) ))
