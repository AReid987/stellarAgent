from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header
from textual.reactive import var
from textual.containers import Container
import asyncio
from textual.easing import Easing
class TuiApp(App):
    """Textual TUI for the AI Gateway."""

    BINDINGS = [
        ("q", "quit", "Quit the app"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("f", "toggle_fullscreen", "Toggle fullscreen"),
    ]

    def compose(self) -> ComposeResult:
        
        yield Header()
        yield Footer()
    
    # CSS_PATH = "tui.tcss"

    # rocket_y = var(20)

    # def compose(self) -> ComposeResult:
    #     """Create child widgets for the app."""
    #     with Container(id="animation-container"):
    #         yield Static("☁️", id="cloud1", classes="cloud")
    #         yield Static("☁️", id="cloud2", classes="cloud")
    #         yield Static("✨", id="stars", classes="stars")
    #         yield Static("🪐", id="planet", classes="planet")
    #         yield Static("🚀", id="rocket", y=self.rocket_y)
    #     with Container(id="title-container", classes="hidden"):
    #         yield Static("AI Gateway", id="title")

    # def on_mount(self) -> None:
    #     """Call run_animation when the app is mounted."""
    #     self.run_animation()

    # async def run_animation(self) -> None:
    #     """Animate the rocket."""
    #     await self.animate(
    #         "rocket_y",
    #         0,
    #         duration=2,
    #         easing=Easing.in_out_cubic,
    #     )
