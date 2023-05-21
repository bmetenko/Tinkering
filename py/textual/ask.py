from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, HorizontalScroll
from textual.widgets import Label, Button, Header, Input

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig

model_name = 'google/flan-t5-xl'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = GenerationConfig(max_new_tokens=400)

global accumulated_text 

accumulated_text= ""

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
        yield HorizontalScroll(VerticalScroll(id="history"))

    def action_submit_prompt(self) -> None:

        global accumulated_text

        text_log = self.query_one(VerticalScroll)

        text_value = self.query_one(Input).value
        try:
            value = str(text_value)
        except ValueError:
            return
        
        self.TITLE = "Loading..."
        
        question = "Question:" + str(value)
        text_log.mount(Label(question))

        accumulated_text += question

        tokens = tokenizer(accumulated_text, return_tensors="pt")
        outputs = model.generate(**tokens, generation_config=config)
        out_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        answer = "Answer:" + " ".join(out_text)
        text_log.mount(Label(answer))

        accumulated_text += answer

        self.query_one(Input).value = ""
        self.TITLE = "A Question App for LLMs"


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(reply)
