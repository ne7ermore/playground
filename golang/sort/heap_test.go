package sort

import (
	"testing"
)

func xTest_heap(t *testing.T) {
	_h := new(Heap_)
	_h.list = []int{2, 4, 1, 6, 3, 7, 31, 12, 5, 8, 21, 11, 9, 102, 10}

	_h.Build()
	_h.Println()

}
