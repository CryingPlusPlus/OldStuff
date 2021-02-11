package main

import "fmt"

//structs
type Student struct {
	name string
	grades []int
	age int
}

//funcs
func (s *Student) getAge() int {
	return s.age
}

func (s *Student) setAge(age int) {
	s.age = age
}

func (s *Student) getAverageGrade() float32 {
	sum := 0
	for _, val := range s.grades {
		sum += val
	}
	return float32(sum) / float32(len(s.grades))
}

func (s *Student) getMaxGrade() int {
	curMax := 0

	for _, val := range s.grades {
		if val > curMax {
			curMax = val
		}
	}

	return curMax
}

//main
func main() {
	s1 := Student{"Ben", []int{80, 69, 40, 90, 97}, 17}

	fmt.Println(s1.getAge())
	s1.setAge(s1.getAge() + 1)
	fmt.Println(s1.age)

	fmt.Println("Average", s1.getAverageGrade())
	fmt.Println("Max:", s1.getMaxGrade())
}