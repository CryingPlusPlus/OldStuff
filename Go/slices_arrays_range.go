package main

import "fmt"

func main() {
	var a []int = []int{1, 2, 3, 4, 5, 23, 45, 7, 23}

	for i, el1 := range a {
		for j, el2 := range a{
			if el1 == el2 && i != j {
				fmt.Println(el1)
			}
		}
	}
}