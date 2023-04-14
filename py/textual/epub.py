import ebooklib
from ebooklib import epub
from textual.app import App
from textual.widgets import Static 
from textual.scroll_view import ScrollView
from textual import events

class MainApp(App):
    def compose(self):
        book = epub.read_epub('test.epub')
        content = ""
        for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content += doc.content.decode('utf-8') + "\n"

        text_box = Static(content)
        scroll_view = ScrollView(text_box)
        yield scroll_view

if __name__ == "__main__":
    app = MainApp()
    app.run()
