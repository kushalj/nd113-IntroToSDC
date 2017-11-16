"""coinflips"""

num_trials = 100000
heads = 0
tails = 0
p_heads = 0.5

for i in 1:num_trials
    random_number = rand()
    if random_number < p_heads
        heads += 1
    else
        tails += 1
    end
end

println("In ", num_trials, " trials there were ", heads, " heads and ", tails, " tails")
println("PERCENT HEADS: ", 100 * heads/num_trials, " percent")
