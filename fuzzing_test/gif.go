package gif

import (
	"bytes"
	"image/gif"
)

func Fuzz(data []byte) int {
	gif.Decode(bytes.NewReader(data))
	return 0
}
