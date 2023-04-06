from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from stopwatch_widget import StopwatchWidget 

class Stopwatch(App):
    """
    # Todo: Docstring
    """
    
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

    def action_toggle_dark(self) -> None:
        """"""
        self.dark = not self.dark

    def action_add_timer(self) -> None:
        """ Adding timer. """
        new_timer = StopwatchWidget()
        self.query_one("#timers").mount(new_timer)
        new_timer.scroll_visible()

    def action_remove_timer(self) -> None:
        timers = self.query("StopwatchWidget")
        if timers:
            timers.last().remove()

    def action_quit(self) -> None:
        quit()

if __name__ == "__main__":
    app = Stopwatch()
    app.run()    
