package main

import "fmt"

func print(str string) {
	fmt.Println(str)
}

func someCalc(a, b int) (erg1, erg2 int) {
	defer fmt.Println("erg1: ", erg1, "erg2: ", erg2) //nimmt die default typen... calc erst im return?
	erg1 = a + b
	erg2 = a - b
	fmt.Println("Before return")
	return 
}

func main() {
	print("Hello World! in almost Python")
	erg1, erg2 := someCalc(1, 2)
	fmt.Println("erg1: ", erg1, "erg2: ", erg2)
}