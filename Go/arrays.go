package main

import "fmt"

func main() {
	var arr [5]int //achtung es sind 5 elemente drinnen und die ELemente haben die default_value vom type
	var arr2 [5]int{0,1,2,3,4}

	sum := 0

	for i := 0; i < len(arr); i++ {
		sum += arr2[i]
	}

	fmt.Println("Sum is ", sum)
	
}