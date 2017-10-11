package main

import (
  "strconv"
  "fmt"
  "math"
  //"./mymath"
)

// a_lat max = 12 m/s^2
// v = 30 m/s

func aLat(v, r float64) float64 {
  return math.Pow(v,2) / r
}


func main() {
  var v float64 = 30
  radii := []float64{50, 31.4, 75, 16}

  for _,r := range radii {
    fmt.Println("a_lat for radius " +
      strconv.FormatFloat(r, 'f', -1, 64) +
      ": " +
      strconv.FormatFloat(aLat(v, r), 'f', -1, 64))
  }
}
