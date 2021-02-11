package main

import "fmt"

func test() {
	fmt.Println("test")
}

func test4(myFunc func(int) int) {
	fmt.Println(myFunc(7))
}

func main() {
	x := test
	test()
	x()

	test2 := func() {
		fmt.Println("Hello World!")
	}
	test2()

	test3 := func(x int) int {
		return x * -1
	}

	fmt.Println(func(x int) int {return x * -2}(8))

	fmt.Println(test3(8))

	test4(test3)
}