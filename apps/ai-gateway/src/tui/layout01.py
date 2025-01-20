from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class TuiScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield Footer(id="footer")

class Layout01App(App):
  def on_ready(self) -> None:
    self.push_screen = TuiScreen()

if __name__ == "__main__":
  app = Layout01App()
  app.run()