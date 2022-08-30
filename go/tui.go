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

func cycle_up(l *tui.List) {
	l.SetSelected((l.Selected() + 1) % l.Length())
	return
}

func cycle_down(l *tui.List) {
	current := l.Selected()

	if (current - 1) < 0 {
		current = current + l.Length()
	}

	l.SetSelected((current - 1) % l.Length())
	return
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

	okay := tui.NewLabel("Everything will be fine.")

	l := tui.NewList()
	l.SetFocused(true)
	l.AddItems("1st row", "2nd row", "3rd row", "4th row", "5th row", "6th row")
	l.SetSelected(0)

	warning := tui.NewLabel("WARNING: TUI overloaded.")
	warning.SetStyleName("warning")

	fatal := tui.NewLabel("FATAL: Frame.")
	fatal.SetStyleName("fatal")

	message1 := tui.NewLabel("This is an ")
	emphasis := tui.NewLabel("important")
	message2 := tui.NewLabel(" message, in general.")
	message := &StyledBox{
		Style: "bsod",
		Box:   tui.NewHBox(message1, emphasis, message2, tui.NewSpacer()),
	}

	emphasis.SetStyleName("emphasis")

	okay2 := tui.NewLabel("Don't forget your towel, and you'll be okay.")

	l2 := tui.NewLabel(`Scroll me with 't' or 'r'.`)

	scroll := tui.NewScrollArea(l2)
	scroll_container := tui.NewVBox(scroll)
	scroll_container.SetBorder(true)

	root := tui.NewVBox(okay, l, warning, fatal, message, okay2)

	root.Append(tui.NewVBox(tui.NewSpacer()))
	root.Append(scroll_container)
	root.Append(tui.NewVBox(tui.NewSpacer()))
	root.SetBorder(true)

	ui, err := tui.New(root)

	if err != nil {
		log.Fatal(err)
	}

	ui.SetTheme(t)
	ui.SetKeybinding("Esc", func() { ui.Quit() })
	ui.SetKeybinding("q", func() { ui.Quit() })
	ui.SetKeybinding("Ctrl+C", func() { ui.Quit() })

	ui.SetKeybinding("p", func() { cycle_up(l) })

	ui.SetKeybinding("o", func() { cycle_down(l) })

	ui.SetKeybinding("t", func() { scroll.ScrollToTop() })
	ui.SetKeybinding("r", func() { scroll.ScrollToBottom() })

	if err := ui.Run(); err != nil {
		log.Fatal(err)
	}

}
