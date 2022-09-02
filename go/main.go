package main

import (
	"fmt"
	"log"
	"os"
	"time"

	tea "github.com/charmbracelet/bubbletea"
)

type model int
type tickMsg time.Time

func tick() tea.Msg {
	time.Sleep(time.Second)
	return tickMsg{}
}

func (m model) Init() tea.Cmd {
	return tick
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg.(type) {
	case tea.KeyMsg:
		return m, tea.Quit
	case tickMsg:
		m -= 1
		if m <= 0 {
			return m, tea.Quit
		}
		return m, tick
	}
	return m, nil
}

func (m model) View() string {
	out := fmt.Sprintf("Hi. This program will exit in %d seconds. Quit sooner wit any key.\n", m)
	return out
}

func main() {
	logFilePath := os.Getenv("BUBBLETEA_LOG")

	if logFilePath != "" {
		if _, err := tea.LogToFile(logFilePath, "simple"); err != nil {
			log.Fatal(err)
		}
	}
}
