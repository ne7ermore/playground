package search

func b_seach(list []int, num int) (index int) {
	temp := len(list)
	var mid int
	for {
		mid = (index + temp) / 2
		if list[mid] == num {
			index = mid
			return
		} else if list[mid] < num {
			index = mid
		} else if list[mid] > num {
			temp = mid
		}
	}
}
