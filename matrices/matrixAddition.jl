

A = [
    [2 5 1]
    [6 9 7.4]
    [2 1 1]
    [8 5 3]
    [2 1 6]
    [5 3 1]
]

B = [
    [7  19  5.1]
    [6.5 9.2 7.4]
    [2.8 1.5 12]
    [8 5 3]
    [2 1 6]
    [2 33 1]
]

println(A+B)

# transpose
println(A.')

# 1-based referencing.
# (not 0-based like some 8-bit relic :) )
println(A[1, 1], A[6, 3])
