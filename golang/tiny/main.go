package main

import (
	"fmt"
)

type field struct {
	name string
}

func (p *field) print() {
	fmt.Println(p.name)
}

func test(p []int) {
	p[0] = 100
	println(&p)
	println(&p[0])
	println()
	for _, n := range p {
		print(n)
	}
	println()
}

func main() {
	p := []int{1, 2, 3, 4, 5}
	// p2 := []int{10, 20, 30, 4, 5, 2}
	for _, n := range p {
		print(n)
	}
	println()
	println(&p)
	println(&p[0])
	println()
	test(p)
	// copy(p2, p)
	for _, n := range p {
		print(n)
	}
	println()
	println(&p)

	i := 1
	println(&i)
	i = 2
	println(&i)

	j := []int{1, 2, 3}
	println(&j)
	j[0] = 30
	println(&j)
}
