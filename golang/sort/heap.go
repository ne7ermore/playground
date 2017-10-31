// Top small heap

package sort

type Heap_ struct {
	list []int
}

func (h *Heap_) Swap(i1, i2 int) {
	h.list[i1], h.list[i2] = h.list[i2], h.list[i1]
}

func (h *Heap_) Compare(i1, i2 int) bool {
	return h.list[i1] > h.list[i2]
}

func (h *Heap_) Println() {
	for _, in := range h.list {
		println(in)
	}
}

func (h *Heap_) Build() {
	for i := len(h.list) / 2; i >= 0; i-- {
		Heap(h, i, len(h.list)-1)
	}

	for i := len(h.list) - 1; i > 0; i-- {
		h.Swap(0, i)
		Heap(h, 0, i)
	}
}

func Heap(h *Heap_, index, end int) {
	length := len(h.list[:end])
	var child int
	for {
		if index*2+1 >= length {
			break
		}

		child = index*2 + 1
		if child+1 < length && h.Compare(child, child+1) {
			child++
		}

		if h.Compare(child, index) {
			break
		}

		h.Swap(index, child)
		index = child
	}
}
