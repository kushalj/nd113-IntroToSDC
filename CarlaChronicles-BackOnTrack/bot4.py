""" Back on Track exercises """
from mymath import TAU

# Right now the make_decision function ALWAYS decides to go left.
# Modify this function so it behaves appropriately.

def make_decision(L1, L2, L3, L4):
    direction = "L"
    if L1 + L2 < L3 + L4:
        direction = "R"
    return direction


##########################################################
#
# The code below is similar to the code that Udacity
# will use to test the correctness of your submission.
# You don't need to modify it but it may
# be helpful to look at for Python syntax help
#
def test_make_decision():
    # start by initializing this to 0
    number_correct = 0

    # TEST 1, should return "R" since left path has
    # length 5 which is < left path with length 8
    length_1 = 2
    length_2 = 3
    length_3 = 4
    length_4 = 4

    decision = make_decision(length_1, length_2, length_3, length_4)

    if decision == "R":
        # Test 1 passes
        number_correct = number_correct + 1

    # TEST 2, should return "L" since right path still
    # has length 5 but left is only 3.
    length_3 = 1
    length_4 = 2

    decision = make_decision(length_1, length_2, length_3, length_4)
    if decision == "L":
        # Test 2 passes
        number_correct = number_correct + 1

    if number_correct == 2:
        all_correct = True
    else:
        all_correct = False

    return all_correct

if test_make_decision():
    print("Nice work! Your function passed both test cases.")
else:
    print("Not quite. Your function didn't pass both test cases.")
