package main

import (
	"fmt"
)

func main() {
	x := 15
	a := &x //memory adresse

	fmt.Println(x, a)
	fmt.Println("*a", *a)
}