# Get Tau and other custom maths bits
include("mymath.jl")
importall MyMath

function getDiameter(dist_before_turn, dist_after_turn)
    circumference = dist_after_turn - dist_before_turn
    diameter = 2 * (circumference/τ)
end

println( string("Diameter: ", getDiameter(1.0, 6.0)) )
