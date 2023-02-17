import pyxel as px

APP_WIDTH = 600
APP_HEIGHT = 800
APP_NAME = "BASE UI"

class App:

    def __init__(self) -> None:
        px.init(
            APP_WIDTH,
            APP_HEIGHT,
            APP_NAME
        )

        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

    def draw(self):
        px.text(200, 200, "Base UI", px.frame_count % 16)
        px.tri(0, 200, 200, 300, 0, 100, px.COLOR_BROWN)



App()