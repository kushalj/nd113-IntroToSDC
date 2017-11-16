""" bayes.jl"""


# The complement function takes in the probability of an event, P(A).
function complement(p_A)

    ## TODO: Change the value of complement
    ## So that it calculates the complement of any variable p_A
    complement = 1.0 - p_A

    return complement
end

## TODO: Change this test value and test out your code!
p_test = 0.2

# Running your code with the p_test value
complement_test = complement(p_test)
@printf( "Your function returned that the complement of %.3f is %.3f\n",
        p_test, complement_test
        )


## Complete this joint function
function joint(p_A, p_B)

    ## TODO: Change the value of joint_p
    ## so that it calculates the joint probability of
    ## any variables p_A, p_B, WHEN THOSE PROBABILITIES
    ## ARE INDEPENDENT (this code wouldn't work
    ## for probabilities that depend on each other).
    joint = p_A * p_B

    return joint
end

## TODO: Test out your code
## Define test probabilities and write print statements to test
## the output of your function!
p_a_test = 0.2
p_b_test = 0.4
j = joint(p_a_test, p_b_test)

@printf("Your function returned that the joint probability is: %.3f\n", j)


# The inputs to total probability are given descriptive names

function total_probability(p_disease, p_pos_given_disease, p_pos_given_no_disease)

    ## TODO: Change the value of total so that it calculates the
    ## total probability of a positive test result
    ## You may use other variable in this function as well as long
    ## as total is correct
    total = joint(p_disease, p_pos_given_disease) + joint(complement(p_disease), p_pos_given_no_disease)

    return total
end


## TODO: Change these test values, run your function, and write print statements to test your code
## Answer the question: what is the probability of a positive test result given the following values?
p_disease = 0.2
p_pos_given_disease= 0.6
p_pos_given_no_disease= 0.6

tot = total_probability(p_disease, p_pos_given_disease, p_pos_given_no_disease)
@printf("Your function returned that the total probability is: %.3f\n", tot)

tot = total_probability(0.2, 0.6, 0.6)
@printf("Exercise 4: p_disease = 0.2, p_pos_given_disease= 0.6, and p_pos_given_no_disease= 0.6: %.3f\n", tot)


# Given three input probabilities, complete this function
# so that it returns the posterior probability

function bayes(p_A, p_B_given_A, p_notB_given_notA)

    ## TODO: Calculate the posterior probability
    ## and change this value
    joint_A = p_A * p_B_given_A
    joint_notA = (1.0 - p_A) * (1.0 - p_notB_given_notA)
    total_A = joint_A + joint_notA
    posterior = joint_A/total_A

    joint_A = p_A * p_B_given_A
    posterior = joint_A / (joint_A + joint(1.0 - p_A, 1.0 - p_notB_given_notA))

    return posterior
end


## TODO: Change these values, run your code with them, and use print
## statements to see the output of your function and get feedback
p_A = 0.2
p_B_given_A = 0.9
p_notB_given_notA = 0.5

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
@printf("Your function returned that the posterior is: %.3f\n", posterior)

p_A = 0.3
p_B_given_A = 0.7
p_notB_given_notA = 0.9

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
@printf("Your function returned that the posterior is: %.3f\n", posterior)
