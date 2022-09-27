package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func swap(x *float64, y *float64) {
	// Benefit: No need to return and create new objects,
	// Hence more efficient computationally.
	*x, *y = *y, *x
}

func printSwap() {
	fmt.Println("---")
	fmt.Println("Pointer based swap example:")
	a := 123.5
	b := 345.2

	fmt.Printf("a originally: %.1f\nb originally %.1f \n", a, b)

	swap(&a, &b)

	fmt.Printf("a now: %.1f\nb now %.1f \n", a, b)
	fmt.Println("---")
}

func main() {

	printSwap()

	stdReader := bufio.NewReader(os.Stdin)
	// fmt.Print("Enter some text: ")
	// input, other_var := stdReader.ReadString('\n')
	// fmt.Print("Input: ", input, "other val: ", other_var, "\n")
	// if other_var == nil {
	// 	fmt.Println("No error occurred.")
	// }

	var now = time.Now()
	fmt.Printf("Current time: %s \n", now.Format(time.ANSIC))

	fmt.Println("Add how many years to start time:")
	inputY, _ := stdReader.ReadString('\n')
	if inputY != "" {
		intY, errY := strconv.ParseInt(strings.TrimSpace(inputY), 10, 64)
		if errY == nil {
			now = now.AddDate(0, 0, int(intY))
		} else {
			fmt.Println(
				"Input could not be parsed as integer,",
				"time delta not modified for years.",
			)
		}
	}

	fmt.Println("Add how many days to start time:")
	inputD, _ := stdReader.ReadString('\n')
	if inputD != "" {
		intD, errD := strconv.ParseInt(strings.TrimSpace(inputD), 10, 32)
		if errD == nil {
			now = now.AddDate(int(intD), 0, 0)
		} else {
			fmt.Println(
				"Input could not be parsed as integer,",
				"time delta not modified for days.",
			)
		}
	}

	fmt.Printf("Final Time: %s\n", now)

}
