package main

import (
	"fmt"
	"math"
	"math/rand"
)

func getRandomInt(a int, b int) int {
	return rand.Intn(b)
}

func main() {
	fmt.Println("sqrt of 5 is", math.Sqrt(5))
	//fmt.Println("Random 0, 100", getRandomInt(0, 100)) 
}