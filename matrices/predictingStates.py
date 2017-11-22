# The predict_state function should take in a state
# and a change in time, dt (ex. 3 for 3 seconds)
# and it should output a new, predicted state
# based on a constant motion model
# This function also assumes that all units are in m, m/s, s, etc.

def predict_state(state, dt):
    # Assume that state takes the form [x, vel] i.e. [0, 50]

    ## TODO: Calculate the new position, predicted_x
    ## TODO: Calculate the new velocity, predicted_vel
    ## These should be calculated based on the contant motion model:
    ## distance = x + velocity*time

    distance = state[0] + state[1] * dt
    predicted_x = distance
    predicted_vel = state[1]

    # Constructs the predicted state and returns it
    predicted_state = [predicted_x, predicted_vel]
    return predicted_state


## TODO: Click Test Run!

# A state and function call for testing purposes - do not delete
# but feel free to change the values for the test variables
test_state = [10, 3]
test_dt = 5

test_output = predict_state(test_state, test_dt)

print(test_output)
