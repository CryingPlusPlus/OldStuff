package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	fmt.Println("IN welchem Jahr wurdest du geboren: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input, _ := strconv.ParseInt(scanner.Text(), 10, 64)



	fmt.Printf("Du wirst  %d Jahre alt sein", 2020 - input)
}