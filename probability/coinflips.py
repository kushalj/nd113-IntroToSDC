""" coinflips"""
import random as rd

num_trials = 100000
heads = 0
tails = 0
p_heads = 0.5

for i in range(num_trials):
    random_number = rd.random()
    if random_number < p_heads:
        heads = heads + 1
    else:
        tails += 1

print("In", num_trials, "trials there were", heads, "heads and", tails, "tails")
print("PERCENT HEADS:", 100 * heads/num_trials, "percent")
