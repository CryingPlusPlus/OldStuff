package main

import "fmt"


func fuck(num int) int {
	if num == 0 {
		return 1
	} else {
		return num * fuck(num - 1)
	}
}

func main() {
	fmt.Println("Fukultät von 5: ")
	fmt.Println(fuck(5))
}