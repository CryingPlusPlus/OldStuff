package main

import "fmt"


func fibo(anzahl int64) map[int64]int64 {
	var reihe map[int64]int64 = map[int64]int64{0:0, 1:1}

	if anzahl >= 2{
		for i:=2; i<anzahl; i++ {
			reihe[len(reihe)] = reihe[len(reihe) - 2] + reihe[len(reihe) - 1]
		}
	} else {
		fmt.Println("wrong")
	}
	return reihe
}

func main() {
	fmt.Println("Fibbonacci")
	reihe := fibo(499)
	fmt.Println(reihe[len(reihe) - 1])
}