package main

import (
  "strconv"
  "fmt"
  "./mymath"
)

func main() {
  fmt.Println("Diameter: " + strconv.FormatFloat(getDiameter(1.0, 6.0), 'f', -1, 64))
}

func getDiameter(distBeforeTurn, distAfterTurn float64) float64 {
  circumference := distAfterTurn - distBeforeTurn
  diameter := 2 * (circumference/mymath.Tau)
  return diameter
}
