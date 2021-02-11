package main

import "fmt"

func main() {

	//maps are very fucking fast instant fast super fast faaaaaaaaaaaasssssstttt
	var mp map[string]int = map[string]int{
		"apple":1,
		"pear":3,
		"orange":9,
	}
	fmt.Println(mp["apple"])
	fmt.Println(mp)

	delete(mp, "apple")

	val, ok := mp["apple"]

	fmt.Println("Val: ", val, "ok: ", ok)
	fmt.Println(len(mp))
}