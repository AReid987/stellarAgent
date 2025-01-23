import typer
from typing import Optional

app = typer.Typer()

@app.command()
def start():
    typer.echo("Starting AI Gateway...")
    
def main():
    app()

if __name__ == "__main__":
    typer.run(main)
    