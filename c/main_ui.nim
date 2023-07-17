# File: main_ui.nim
# import nimx/window
# import nimx/text_field

# proc startApp() =
#     var root = newWindow(newRect(40, 40, 800, 600))

#     let label = newLabel(newRect(20, 20, 150, 20))
#     label.text = "Nimx window"
#     root.addSubview(label)

# runApplication:
#     # first maybe but still breaks: brew install sdl2{,_gfx,_image,_mixer,_net,_ttf} // M1
#     # nim c -r --threads:on main_ui.nim
#     startApp()

import nigui

app.init()

var window = newWindow("Main")
window.width = 600
window.height = 450

var mainContainer = newLayoutContainer(Layout_Vertical)
mainContainer.padding = 6
window.add(mainContainer)

window.onKeyDown = proc(event: KeyboardEvent) =
  if event.key == Key_Escape:
    window.dispose()


# Also breaks even with
# nim c --passL:"-L/opt/homebrew/Cellar/gtk+3/3.24.38/lib/" --run --define:nimDebugDlOpen main_ui.nim


window.show()
app.run()