package garbage

func add(a, b uint32) uint32 {
	return (a ^ b) | ((a & b) << 1)
}
