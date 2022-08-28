package main

import (
	"fmt"

	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	fmt.Println(series.New([]string{"z", "y", "d", "e"}, series.String, "col"))

	a := map[string]series.Type{
		"A": series.String,
		"D": series.Bool,
	}

	frame := dataframe.New(
		series.New([]string{"A", "B", "C"}, series.String, "Box"),
		series.New([]int{3, 2, 1}, series.Int, "Size"),
		series.New([]bool{true, false, false}, series.Bool, "Open"),
		series.New([]bool{false, false, false}, series.Bool, "Damaged"),
	)

	fmt.Println(a)
	fmt.Println(frame)

	type _Box struct {
		Box_Name string
		Size     int
		Open     bool
		Damaged  bool
	}

	boxes := []_Box{
		{"A", 3, true, false},
		{"B", 2, false, false},
		{"C", 1, false, false},
	}

	boxesDf := dataframe.LoadStructs(boxes)

	fmt.Println(boxesDf)

	// Properties
	fmt.Println(boxesDf.Dims())
	fmt.Println(boxesDf.Types())
	fmt.Println(boxesDf.Names())
	fmt.Println(boxesDf.Nrow())
	fmt.Println(boxesDf.Ncol())

	fmt.Println()
}
