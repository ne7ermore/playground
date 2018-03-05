package sort

import (
	"math/rand"
	"testing"
	"time"
)

func Test_bitsort(t *testing.T) {
	max := 1000000
	list := make([]uint, max)
	for i, v := range rand.Perm(max) {
		list[i] = uint(v)
	}

	start := time.Now()
	bitsort(list, uint(max))
	end := time.Now()

	println(end.Sub(start) / time.Millisecond)
}
