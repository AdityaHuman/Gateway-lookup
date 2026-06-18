import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

def display_results(result: dict):
    table = Table(title="Gateway Lookup Results")
    table.add_column("Field")
    table.add_column("Value")
    for k, v in [
        ("Domain", result["domain"]),
        ("URL", result["url"]),
        ("Status", str(result["status_code"])),
        ("Gateways", ", ".join(result["gateways"])),
        ("Captcha", "Yes" if result["captcha"] else "No"),
        ("Cloudflare", "Yes" if result["cloudflare"] else "No"),
        ("Time", f"{result['time_taken']}s"),
    ]:
        table.add_row(k, v)
    console.print(table)

def save_json(result: dict):
    Path("results").mkdir(exist_ok=True)
    filename = Path("results") / f"{result['domain'].replace('.', '_')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
    return filename
