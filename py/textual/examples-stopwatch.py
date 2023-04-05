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
        ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield Container(
            StopwatchWidget(),
            StopwatchWidget(),
            StopwatchWidget(),
        )

    def action_toggle_dark(self) -> None:
        """"""
        self.dark = not self.dark

if __name__ == "__main__":
    app = Stopwatch()
    app.run()    
