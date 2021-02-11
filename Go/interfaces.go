package main

import (
	"fmt"
	"math"
)

//interfaces----------------------------------------------------------------
type area interface {
	getArea() float64
}

//types---------------------------------------------------------------------
type Rect struct {
	width float64
	height float64
}

type Circle struct {
	radius float64
}

//methods----------------------------------------------------------------------
func (r Rect) getArea() float64 {
	return r.width * r.height
}

func (c Circle) getArea() float64 {
	return math.Pi * c.radius * c.radius
}

//main---------------------------------------------------------------------------
func main() {
	c1 := Circle{34.1}
	r1 := Rect{3, 4}

	//fmt.Println(c1.getArea())
	//fmt.Println(r1.getArea())
	areas := []area{c1, r1}
	fmt.Println(areas)

	for _, area := range areas {
		fmt.Println(area.getArea())
	}
}