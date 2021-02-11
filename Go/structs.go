package main

import "fmt"


//types
type Point struct {
	x int32
	y int32
}

type Circle struct {
	radius float64
	*Point
}


//funcs
func changeX(pt *Point) {
	pt.x = 7
}


//main
func main() {
	var p1 Point = Point{1, 2}
	var p2 Point = Point{-5, 7}

	fmt.Println(p1.x, p2)

	p1.x = 7

	fmt.Println(p1.x, p2)

	p3 := Point{x:3}
	fmt.Println(p3)
	p4 := &Point{1, 3}
	fmt.Println("p4:", *p4)
	changeX(p4)
	fmt.Println("p4:", *p4)

	c1 := &Circle{3.14, &Point{1, 2}}
	fmt.Println("c1", c1.radius, c1.x, c1.y)
	fmt.Println("c1: ", c1)
}