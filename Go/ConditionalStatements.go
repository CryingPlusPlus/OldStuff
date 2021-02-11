package main

import "fmt"

func main() {
	var age uint8 = 15

	if age >= 18 {
		fmt.Println("Du kannst alleine fahren")
	} else if age >= 14 {
		fmt.Println("Du kannst mit einer Begleitperson fahren")
	} else {
		fmt.Println("Du kannst nicht fahren")
	}
}