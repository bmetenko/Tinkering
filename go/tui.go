package main

import (
	"log"

	"github.com/marcusolsson/tui-go"
)

type StyledBox struct {
	Style string
	*tui.Box
}

func (s *StyledBox) Draw(p *tui.Painter) {
	p.WithStyle(s.Style, func(p *tui.Painter) {
		s.Box.Draw(p)
	})
}

func main() {

	t := tui.NewTheme()
	normal := tui.Style{Bg: tui.ColorWhite, Fg: tui.ColorBlack}

	t.SetStyle("normal", normal)
	t.SetStyle("list.item", tui.Style{Bg: tui.ColorYellow, Fg: tui.ColorCyan})
	t.SetStyle("list.item.selected", tui.Style{Bg: tui.ColorRed, Fg: tui.ColorYellow})
	t.SetStyle("label.warning", tui.Style{Bg: tui.ColorWhite, Fg: tui.ColorBlack})
	t.SetStyle("label.fatal", tui.Style{Bg: tui.ColorDefault, Fg: tui.ColorRed})
	t.SetStyle("label.emphasis", tui.Style{Bold: tui.DecorationOn, Underline: tui.DecorationOn, Bg: tui.ColorRed})
	t.SetStyle("bsod", tui.Style{Bg: tui.ColorCyan, Fg: tui.ColorWhite})

	okay := tui.NewLabel("Everything is fine.")

	l := tui.NewList()
	l.SetFocused(true)
	l.AddItems("First row", "Second row", "Third row", "Fourth row", "Fifth row", "Sixth row")
	l.SetSelected(0)

	warning := tui.NewLabel("WARNING: This is a warning")
	warning.SetStyleName("warning")

	fatal := tui.NewLabel("FATAL: Cats and dogs are now living together.")
	fatal.SetStyleName("fatal")

	message1 := tui.NewLabel("This is an ")
	emphasis := tui.NewLabel("important")
	message2 := tui.NewLabel(" message from our sponsors.")
	message := &StyledBox{
		Style: "bsod",
		Box:   tui.NewHBox(message1, emphasis, message2, tui.NewSpacer()),
	}

	emphasis.SetStyleName("emphasis")

	okay2 := tui.NewLabel("Everything is still fine.")

	root := tui.NewVBox(okay, l, warning, fatal, message, okay2)

	ui, err := tui.New(root)

	if err != nil {
		log.Fatal(err)
	}

	ui.SetTheme(t)
	ui.SetKeybinding("Esc", func() { ui.Quit() })
	ui.SetKeybinding("q", func() { ui.Quit() })
	ui.SetKeybinding("Ctrl+C", func() { ui.Quit() })

	ui.SetKeybinding("p", func() {
		// println(l.Selected())
		l.SetSelected((l.Selected() + 1) % l.Length())
		return
	})

	ui.SetKeybinding("o", func() {
		// println(l.Selected())
		current := l.Selected()
		if current-1 == -1 {
			current = l.Length()
		}

		l.SetSelected((current - 1) % l.Length())

		return
	})

	if err := ui.Run(); err != nil {
		log.Fatal(err)
	}

}
