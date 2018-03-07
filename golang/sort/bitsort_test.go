package sort

import (
	"math/rand"
	"testing"
	"time"
)

func Test_bitsort(t *testing.T) {
	max := 10000
	list := make([]uint, max)
	for i, v := range rand.Perm(max) {
		list[i] = uint(v)
	}
	println(list[0])
	list = list[1:]
	start := time.Now()
	res := bitsort(list, uint(max))

	end := time.Now()
	for _, r := range res {
		print(r)
		print(" ")
	}
	println("time cost")
	println(end.Sub(start) / time.Millisecond)
}
