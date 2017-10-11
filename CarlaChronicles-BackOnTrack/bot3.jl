# Get Tau and other custom maths bits
include("mymath.jl")
importall MyMath

# a_lat max = 12 m/s^2
# v = 30 m/s

function a_lat(v, r)
    return v^2/r
end

v = 30
for r in [50, 31.4, 75, 16]
    println( string("a_lat for radius ", r, ": ", a_lat(v, r)) )
end
