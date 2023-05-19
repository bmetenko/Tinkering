from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Label, Button, Header, Input


class QuestionApp(App[str]):
    CSS = """
    Screen {
        layout: grid;
        padding: 2;
    }
    #question {
        width: 100%;
        height: 100%;
        content-align: center bottom;
        text-style: bold;
    }

    Button {
        width: 100%;
    }
    """

    BINDINGS = [
        Binding("enter", "submit_prompt", "submit", show=False, priority=True),
        ("d", "toggle_dark", "Toggle dark mode")
        ]

    data_pool = []

    TITLE = "A Question App for LLMs"
    SUB_TITLE = "Demo"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Label("What's your question?", id="question")
        yield Input(placeholder="Type it here")
        yield VerticalScroll(id="history")

    def action_submit_prompt(self) -> None:
        text_log = self.query_one(VerticalScroll)

        text_value = self.query_one(Input).value
        try:
            value = str(text_value)
        except ValueError:
            return
        
        text_log.mount(Label(str(value)))

        self.query_one(Input).value = ""


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(reply)
