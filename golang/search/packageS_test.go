package search

import "testing"

func TestSearch(t *testing.T) {
	ss := []*dis{&dis{1.1, 2.3}, &dis{2.5, 3.3}, &dis{3.6, 4.3}, &dis{5.5, 9.3}}
	res := zoneSearch(ss, 10.1, 10.4)
	for _, s := range res {
		println(s.start)
	}
}
