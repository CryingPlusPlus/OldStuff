package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Basic Operators: +, -, *, /, %")
	fmt.Println("Auf beiden Seiten eines Operators muss der gleiche Typ stehen")

	var x int8 = 4
	var y float32 = 5

	answer := float32(x) / y //knovertieren einfach mit type()
 
	fmt.Println(answer)

	fmt.Println("Int / Int floored die Gleichung, kein Runden und keine floaten")
	var a int = 4
	var b int = 9

	fmt.Println(b / a)
	//math operations mit math library
	


}