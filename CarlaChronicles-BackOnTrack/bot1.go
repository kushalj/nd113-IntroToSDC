package main

import (
  "strconv"
  "fmt"
  "math"
)

// Tau not Pi
const Tau = math.Pi * 2

func main() {
  var d float64 = 100
  var r = d/2
  circumference := Tau * r
  fmt.Println("Circumference: " + strconv.FormatFloat(circumference, 'f', -1, 64))
}
