package main

import "fmt"

func main() {
	var slice []int = []int{0,1,2,3,4,5,6,7,8,9}
	slice = append(slice, 10) //returned ein neuen slice
	fmt.Println(slice)

	//anderer Weg
	slice2 := make([]int, 5) //macht einen slice der Länge 5 mit den default typen
	fmt.Println(slice2)

	//test
	slice3 := make([]int, 0) //ca. äquivalt zu slice3 = []
	fmt.Println(slice3)
}