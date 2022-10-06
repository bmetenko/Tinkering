package main

import (
	"fmt"
	"image/color"
	"log"
	"os"

	"gioui.org/app"
	"gioui.org/font/gofont"
	"gioui.org/io/system"
	"gioui.org/layout"
	"gioui.org/op"
	"gioui.org/text"
	"gioui.org/widget/material"
)

func main() {
	go func() {
		window := app.NewWindow()
		err := run(window)
		if err != nil {
			fmt.Println("Main app window crashed.")
			log.Fatal(err)
		}
		os.Exit(0)
	}()

	app.Main()
}

func run(w *app.Window) error {
	theme := material.NewTheme(gofont.Collection())
	var ops op.Ops

	// Setup event loop
	for {
		e := <-w.Events()
		switch e := e.(type) {
		case system.DestroyEvent:
			return e.Err
		case system.FrameEvent:
			gtx := layout.NewContext(&ops, e)

			title := material.H1(theme, "Hello from Gio UI.")
			color := color.NRGBA{R: 14, G: 125, B: 75, A: 255}
			title.Alignment = text.Start
			title.Color = color
			title.TextSize = 35
			title.Layout(gtx)

			e.Frame(gtx.Ops)
		}
	}
}
