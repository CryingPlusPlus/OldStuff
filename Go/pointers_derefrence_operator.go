package main

import "fmt"

func main() {
	x := 7
	fmt.Println("Memory Location of x:", &x)

	y := &x
	fmt.Println("x:", x)
	*y++
	fmt.Println("x:", x)
	fmt.Println("y Information:\ny:", y, "&y:", &y, "*y:", *y)

	// & gibt dir die Location im Ram... * gibt dir den Inhalt einer Location im Ram
}