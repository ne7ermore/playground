package routine

func reint_2(a int) chan int {
	c := make(chan int)
	go func(a int) {
		c <- a
	}(a)
	return c
}

func refloat_2(a float32) chan float32 {
	c := make(chan float32)
	go func(a float32) {
		c <- a
	}(a)
	return c
}

func para() {
	c := reint_2(123)
	f := refloat_2(123.3)

	println(<-c)
	println(<-f)
}
