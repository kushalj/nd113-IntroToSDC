package main

import "fmt"

func main() {
	var i = 5

	if i > 0 {
		fmt.Println("positive")
	} else if i < 0 {
		fmt.Println("negative")
	} else {
		fmt.Println("zero")
	}

	var status = 'a'

	if status == 'a' {
		fmt.Println("accelerating")
	} else if status == 'n' {
		fmt.Println("neutral")
	} else {
		fmt.Println(".")
	}

}
