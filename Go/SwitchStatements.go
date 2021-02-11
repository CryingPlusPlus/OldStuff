package main

import "fmt"

func main() {
	i := 1

	switch i {
	case 0:
		fmt.Println(0)
	case 1:
		fmt.Println(1)
	default:
		fmt.Println("Nicht 0 oder 1")
	}
	//kann man statt if else if else verwenden
	switch {
	case i > 0:
		fmt.Println("big")
	case i < 0:
		fmt.Println("smol")
	default:
		fmt.Println("not big not smol")
	}	
}