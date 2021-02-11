package main

import (
	"fmt"
)

func add(x, y float64) float64 {
	return x + y
} 

func main() {
	// var nr1 float64 = 3.14
	// var nr2 float64 = 6.489

	// var nr1, nr2 float64 = 3.14, 6.489
	// fmt.Println(add(nr1, nr2))

	w1, w2 := "Hello", "there"

	fmt.Println(w1, w2)
}