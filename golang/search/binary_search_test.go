package search

import (
	"testing"
)

func Test_bs(t *testing.T) {
	list := []int{2, 4, 6, 7, 8, 9, 11, 15, 18, 21, 31, 64}
	println(b_seach(list, 64))
}
