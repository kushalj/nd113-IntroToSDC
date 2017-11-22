from functions import predict_state

# predict_state takes in a state and a change in time, dt
# So, a call might look like: new_state = predict_state(old_state, 2)

# The car starts at position = 0, going 60 m/s
# The initial state:
initial_state = [10, 60]

# After 2 seconds:
state_est1 = predict_state(initial_state, 2)

# 3 more seconds after the first estimated state
state_est2 = predict_state(state_est1, 3)

## TODO: Use the predict_state function
## and the above variables to calculate the following states
## (And change their value from 0 to the correct state)

## Then, click Test Run to see your results!

## 1 more second after the second state estimate
state_est3 = predict_state(state_est2, 1)

## 4 more seconds after the third estimated state
state_est4 = predict_state(state_est3, 4)

print(state_est4)
