import pyxel as px

APP_WIDTH = 600
APP_HEIGHT = 800
APP_NAME = "BASE UI"

APP_CHARACTER_HW = (100, 100)
APP_CHARACTER_START = (
    APP_WIDTH/2,
    APP_HEIGHT/2
)
APP_CHARACTER_STEP = 10

# rect(x, y, w, h, col)
TOP_BAR = (0,0, APP_WIDTH, APP_HEIGHT / 6, px.COLOR_GREEN)

class App:

    def __init__(self) -> None:
        px.init(
            APP_WIDTH,
            APP_HEIGHT,
            APP_NAME
        )

        self.c_x, self.c_y = APP_CHARACTER_START


        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btnp(px.KEY_A):
            if self.c_x > 0 and self.c_x < APP_WIDTH:
                self.c_x -= APP_CHARACTER_STEP

        if px.btnp(px.KEY_W):
            if self.c_y > 0 and self.c_y < (APP_HEIGHT - APP_HEIGHT/6):
                self.c_y -= APP_CHARACTER_STEP

        if px.btnp(px.KEY_S):
            if self.c_y > 0 and self.c_y < (APP_HEIGHT - APP_HEIGHT/6):
                self.c_y += APP_CHARACTER_STEP

        if px.btnp(px.KEY_D):
            if self.c_x > 0 and self.c_x < APP_WIDTH:
                self.c_x += APP_CHARACTER_STEP

    def draw(self):
        px.cls(0)
        px.rect(*TOP_BAR)
        px.tri(0, 200, 200, 300, 0, 100, px.COLOR_BROWN)
        px.tri(100, 300, 150, 350, 150, 300, px.COLOR_CYAN)
        px.tri(0, 75, 150, 225, 300, 75, px.COLOR_BROWN)

        px.rect(
            self.c_x, 
            self.c_y, 
            APP_CHARACTER_HW[0],
            APP_CHARACTER_HW[1],
            px.COLOR_DARK_BLUE
            )



App()