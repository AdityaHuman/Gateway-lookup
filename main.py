import typer
from rich.console import Console
from scanner import scan_website
from utils import display_results, save_json

app = typer.Typer()
console = Console()

@app.command()
def lookup(domain: str, save: bool = False):
    result = scan_website(domain)
    if not result["success"]:
        console.print(f"[red]Error:[/red] {result['error']}")
        raise typer.Exit(1)
    display_results(result)
    if save:
        console.print(f"[green]Saved:[/green] {save_json(result)}")

if __name__ == "__main__":
    app()
