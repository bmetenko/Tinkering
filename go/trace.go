package main

import (
	"fmt"

	"github.com/felixge/fgtrace"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	defer fgtrace.Config{Dst: fgtrace.File("fgtrace.json")}.Trace().Stop()

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
}
