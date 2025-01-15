from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.reactive import var
from textual.containers import Container
import asyncio

class TuiApp(App):
    """Textual TUI for the AI Gateway."""

    CSS_PATH = "tui.tcss"

    rocket_y = var(20)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with Container(id="animation-container"):
            yield Static("☁️", id="cloud1", classes="cloud")
            yield Static("☁️", id="cloud2", classes="cloud")
            yield Static("✨", id="stars", classes="stars")
            yield Static("🪐", id="planet", classes="planet")
            yield Static("🚀", id="rocket", y=self.rocket_y)
        with Container(id="title-container", classes="hidden"):
            yield Static("AI Gateway", id="title")
