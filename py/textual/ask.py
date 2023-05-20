from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Label, Button, Header, Input

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig

model_name = 'google/flan-t5-xl'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = GenerationConfig(max_new_tokens=200)

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
        
        self.TITLE = "Loading..."
        
        text_log.mount(Label(str(value)))

        tokens = tokenizer(value, return_tensors="pt")
        outputs = model.generate(**tokens, generation_config=config)
        out_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        text_log.mount(Label(" ".join(out_text)))

        self.query_one(Input).value = ""
        self.TITLE = "A Question App for LLMs"


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(reply)
