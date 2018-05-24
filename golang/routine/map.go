package routine

func check_map() {
	m := map[string]map[string]string{
		"a1": {
			"b2": "1",
			"c2": "2",
		},
		"b1": {
			"a2": "3",
			"d2": "4",
		},
		"c1": {
			"e2": "5",
			"f2": "6",
		},
	}
	println(ckeck(m, "e2"))
}

func ckeck(m map[string]map[string]string, p string) bool {
	c := make(chan bool)

	for _, subm := range m {
		go func(subm map[string]string, p string) {
			for k, _ := range subm {
				if k == p {
					c <- true
				} else {
					c <- false
				}
			}
			close(c)
		}(subm, p)
	}

	for i := range c {
		if i == true {
			return true
		}
	}
	return false
}
