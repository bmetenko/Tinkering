package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {

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
		}
	}

	fmt.Println("Add how many days to start time:")
	inputD, _ := stdReader.ReadString('\n')
	if inputD != "" {
		intD, errD := strconv.ParseInt(strings.TrimSpace(inputD), 10, 32)
		if errD == nil {
			now = now.AddDate(int(intD), 0, 0)
		}
	}

	fmt.Printf("Final Time: %s\n", now)

}
