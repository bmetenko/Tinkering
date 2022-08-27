
import time

import pytermgui as ptg
import pytermgui.markup
from pytermgui.markup import aliases

def macro_time(fmt: str) -> str:
    return time.strftime(fmt)

ptg.tim.define("!curr_time", macro_time)

ptg.tim.alias("wm-title", "blue @141")

with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(
        ptg.Window(
            "[wm-title]My first window!",
            "[bold]The time is:[/]\n\n[!curr_time 75]%c",
            "",
            ["Exit", lambda *_: manager.exit()],
            )
    )