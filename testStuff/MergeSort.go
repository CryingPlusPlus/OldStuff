package main

import (
	"fmt"
	"math/rand"
	"time"
)

func halfAList(input map[int]int) (map[int]int, map[int]int) {
	leni := len(input)
	a := map[int]int{}
	b := map[int]int{}
	for i:=0; i<leni/2; i++ {
		a[i] = input[i]
	}
	lena := len(a)
	for i:=0; i+lena<leni; i++ {
		b[i] = input[i+lena]
	}
	return a, b
}

func mergeSort(input map[int]int) map[int]int {
	if len(input) <= 1 {
		return input
	} else {
		a, b := halfAList(input)
		a = mergeSort(a)
		b = mergeSort(b)
		return merge(a, b)
	}
	
	
}

func merge(a, b map[int]int) map[int]int {
	c := map[int]int{}
	current_a := 0
	current_b := 0
	current_c := 0
	lenA := len(a)
	lenB := len(b)
	for current_a < lenA && current_b < lenB {
		if a[current_a] < b[current_b] {
			c[current_c] = a[current_a]
			current_a++
		} else {
			c[current_c] = b[current_b]
			current_b++
		}
		current_c++
	}
	if current_a == lenA {
		for i:=current_b; i<lenB; i++ {
			c[current_c] = b[i]
			current_c++
			}
	} else {
		for i:=current_a; i<lenA; i++ {
			c[current_c] = a[i]
			current_c++
		}
	}
	return c
}

func main() {
	unsorted := map[int]int{}
	rand.Seed(time.Now().UnixNano())
	for i:=0; i<10; i++ {
		unsorted[i] = rand.Intn(10)
	}
	//fmt.Println(unsorted)
	sorted := mergeSort(unsorted)
	for _, val := range sorted {
		fmt.Println(val)
	}
}