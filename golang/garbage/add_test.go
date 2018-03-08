package garbage

import (
	// "math/rand"
	"testing"
)

func Test_add(t *testing.T) {
	var a, b uint32 = 10001, 9
	res := add(a, b)
	if res != (a + b) {
		t.Fail()
	}
}
