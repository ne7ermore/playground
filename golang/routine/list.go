package routine

func checcc() bool {
	ch := make(chan bool)

	go func() {
		for i := 0; i < 5; i++ {
			if i == 10 {
				ch <- true
			}
		}
		ch <- false
	}()

	return <-ch
}
