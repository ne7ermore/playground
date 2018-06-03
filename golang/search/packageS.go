package search

import (
	"sort"
)

type dis struct {
	start, end float64
}

func zoneSearch(kbs []*dis, start, end float64) []*dis {

	s := sort.Search(len(kbs), func(i int) bool { return kbs[i].end > start })
	e := sort.Search(len(kbs), func(i int) bool { return kbs[i].start > end }) - 1

	if s >= len(kbs) || start > kbs[s].end {
		return nil
	}

	if e < 0 {
		return nil
	}

	if s == e {
		return []*dis{kbs[s]}
	}

	return kbs[s : e+1]
}
