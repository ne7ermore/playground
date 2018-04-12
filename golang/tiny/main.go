package main

import (
	"fmt"
	"time"
)

type field struct {
	name string
}

func (p *field) print() {
	fmt.Println(p.name)
}

func main() {
	data := []*field{{"1"}, {"2"}, {"3"}}

	for _, v := range data {
		go v.print()
	}

	time.Sleep(3 * time.Second)
}
