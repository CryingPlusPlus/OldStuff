package main

import "fmt"



//main
func main() {
	var output string

	for i:=; i<101; i++ {
		output = ""
		if i % 3 == 0 {
			output += "Fizz"
		}
		if i % 5 == 0 {
			output += "Buzz"
		}

		if output != "" {
			fmt.Println(output)
		} else {
			fmt.Println(i)
		}

	}
}