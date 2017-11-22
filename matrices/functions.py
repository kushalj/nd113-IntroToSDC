#---- predict state function --#
def predict_state(state, dt):
    # Assumes a valid state had been passed in
    # Assumes a constant velocity model
    x = state[0]
    new_x = x+state[1]*dt

    # Create and return the new, predicted state
    predicted_state = [new_x, state[1]]
    return predicted_state
