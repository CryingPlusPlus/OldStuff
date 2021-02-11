package main

import "fmt"



func main() {
	var gebJahr int
	fmt.Print("Wann wurdest du geboren? ")
	fmt.Scan(&gebJahr)

	fmt.Print("\nDu wirst ", 2020 - gebJahr, " Jahre alt sein")
	//print("Hello World!")
}