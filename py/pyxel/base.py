import pyxel as px

APP_WIDTH = 600
APP_HEIGHT = 800
APP_NAME = "BASE UI"

APP_CHARACTER_HW = (100, 100)
APP_CHARACTER_START = (
    APP_WIDTH/2,
    APP_HEIGHT/2
)

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
            self.c_x +=1

        if px.btnp(px.KEY_W):
            self.c_y +=1

        if px.btnp(px.KEY_S):
            self.c_x -=1

        if px.btnp(px.KEY_D):
            self.c_y -=1

    def draw(self):
        px.cls(1)
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