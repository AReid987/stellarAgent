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
            yield Static("AI Gateway", id="app-title")
        with Container(id="menu-container", classes="hidden"):
            yield Static("Main Menu", id="main-menu") # Placeholder for the actual menu

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
        
        # Show the title
        self.query_one("#title-container").remove_class("hidden")
        
        # Wait for a bit before showing the main menu
        await asyncio.sleep(1)
        self.query_one("#menu-container").remove_class("hidden")

def run():
    """Run the TUI application."""
    app = TuiApp()
    app.run()

if __name__ == "__main__":
    run()
