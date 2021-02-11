package main

import "fmt"

func main() {
	/*x := 0
	for x < 5 {
		fmt.Println(x)
		x++
	}

	for x := 0; x < 5; x++ {
		fmt.Println(x)
	}*/
	for x := 0; x < 100; x++ {
		if x != 0 && x % 2 == 0 && x % 3 == 0 {
			fmt.Println(x)
			continue
		}
		fmt.Println("N")
	}
}