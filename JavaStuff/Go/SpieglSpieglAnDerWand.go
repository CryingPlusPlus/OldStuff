package main

import (
	"fmt"
)

func reverse( str string ) string {
	var result string
    for _, v := range str { 
        result = string(v) + result 
	} 
	return result
}

func main() {
	var str string
	for ( true ) {
		fmt.Scan( &str )
		if ( str == "quit" ) {
			break;
		}
		if (str == "" ) {
			str = "Spieglein Spieglein an der Wand";
		}
		str = reverse(str)
		fmt.Println(str)
	}
}