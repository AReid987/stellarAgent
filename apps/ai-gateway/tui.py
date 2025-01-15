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
        yield Static("AI Gateway TUI", id="app-title")
        with Container(id="animation-container"):
            yield Static("🚀", id="rocket", y=self.rocket_y)

    async def on_mount(self) -> None:
        """Call animate_rocket when the app is mounted."""
        await self.animate_rocket()

    async def animate_rocket(self) -> None:
        """Animate the rocket launch."""
        rocket = self.query_one("#rocket")
        
        # Initial position
        rocket.styles.y = self.rocket_y
        
        # Animate the rocket upwards
        await rocket.styles.animate("y", 0, duration=5)
        
        # After animation, hide the rocket
        rocket.styles.display = "none"
        
        # Add a message after the animation
        self.query_one("#animation-container").mount(Static("Launched!", id="launch-message"))
        
        # Wait for a bit before removing the message
        await asyncio.sleep(2)
        self.query_one("#launch-message").remove()

def run():
    """Run the TUI application."""
    app = TuiApp()
    app.run()

if __name__ == "__main__":
    run()
