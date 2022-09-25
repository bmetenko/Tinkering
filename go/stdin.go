package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	stdReader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter some text: ")
	input, other_var := stdReader.ReadString('\n')
	fmt.Print("Input: ", input, "other val: ", other_var, "\n")
	if other_var == nil {
		fmt.Println("No error occurred.")
	}
}
