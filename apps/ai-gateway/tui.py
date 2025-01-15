from textual.app import App, ComposeResult
from textual.widgets import Static

class TuiApp(App):
    """Textual TUI for the AI Gateway."""

    CSS_PATH = "tui.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Static("AI Gateway TUI", id="app-title")

def run():
    """Run the TUI application."""
    app = TuiApp()
    app.run()

if __name__ == "__main__":
    run()
