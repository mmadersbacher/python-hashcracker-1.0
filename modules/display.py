from rich.console import Console
from rich.table import Table

console = Console()

def format_stats(mode, password, attempts, duration):
    table = Table(title=f"[green]{mode} erfolgreich[/green]", show_lines=True)
    table.add_column("Passwort", style="cyan", no_wrap=True)
    table.add_column("Versuche", justify="right")
    table.add_column("Dauer (Sekunden)", justify="right")
    table.add_row(password, str(attempts), f"{duration:.2f}")
    console.print(table)
