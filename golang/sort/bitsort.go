package sort

func bitsort(list []uint, max uint) []uint {
	var SHIFT, MASK uint = 32, 0x1f
	var BITSPERWORD int = 32
	top := int(len(list)/BITSPERWORD) + 1

	a := make([]uint, top)
	for i := 0; i < top; i++ {
		a[i] = 0
	}

	for _, member := range list {
		a[member>>SHIFT] |= 1 << (member & MASK)
	}

	var slot int = 0
	for i := uint(0); i < max; i++ {
		if a[i>>SHIFT]&(uint(1)<<(i&MASK)) != 0 {
			list[slot] = i
			slot++
		}
	}

	return list
}
