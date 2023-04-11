from textual import log
from textual.color import Color
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from textual.reactive import reactive

from stopwatch_widget import StopwatchWidget 

class Stopwatch(App):
    """
    # Todo: Docstring
    """

    timer_count = reactive(3)
    
    CSS_PATH = "stopwatch_style.css"

    BINDINGS = [
        ("q", "quit", "Quit app"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_timer", "Add"),
        ("r", "remove_timer", "Remove")
        ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield Container(
            StopwatchWidget(),
            StopwatchWidget(),
            StopwatchWidget(),
            id = "timers"
        )

    def validate_timer_count(self, timer_count: int) -> int:
        """Validate timer value."""
        if timer_count < 0:
            timer_count = 0
        elif timer_count > 20:
            timer_count = 0
        return timer_count

    def action_toggle_dark(self) -> None:
        """"""
        self.dark = not self.dark

    def action_add_timer(self) -> None:
        """ Adding timer. """
        new_timer = StopwatchWidget()
        self.query_one("#timers").mount(new_timer)
        
        alpha = 1 - 0.05 * self.timer_count
        self.timer_count += 1
        new_timer.styles.background = Color(19, 224, 24, a=alpha)

        new_timer.scroll_visible()
        log(f"Added timer {new_timer}")

    def action_remove_timer(self) -> None:
        global count

        timers = self.query("StopwatchWidget")
        
        log("Removed timer: {timers.last()}")
        self.timer_count -= 1

        if timers:
            timers.last().remove()


    def key_space(self) -> None:
        self.bell()

        
    def action_quit(self) -> None:
        log("[bold red]DANGER![/] App called to quit...")
        quit()

if __name__ == "__main__":
    app = Stopwatch()
    app.run()    
