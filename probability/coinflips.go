package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var numTrials = 100000
	var heads = 0
	var tails = 0
	pHeads := 0.5

	rd := rand.New(rand.NewSource(99))
	for i := 1; i <= numTrials; i++ {
		randomNumber := rd.Float64()
		if randomNumber < pHeads {
			heads++
		} else {
			tails++
		}
	}
	fmt.Println("In", numTrials, "trials there were", heads, "heads and", tails, "tails")
	fmt.Println("PERCENT HEADS:", float64(100)*float64(heads)/float64(numTrials), "percent")
}
