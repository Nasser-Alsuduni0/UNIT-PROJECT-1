from rich.console import Console
from rich.table import Table
from rich import box
from .calorie import CalorieTracker
from datetime import date

console = Console()


def show_calorie_summary(calories):
    if not calories:
        console.print("[bold red]No calorie entries recorded yet.[/bold red]")
        return

    total_calories = sum(c.get_calories() for c in calories)
    console.print("\n[bold green]=== Calorie Summary ===[/bold green]")
    console.print(f"[cyan]Total Calories Consumed:[/cyan] {total_calories}")

    today = str(date.today())
    today_calories = sum(c.get_calories()
                         for c in calories if c.get_date() == today)
    console.print(
        f"[cyan]Calories Consumed Today ({today}):[/cyan] {today_calories}")

   
    date_totals = {}
    for c in calories:
        d = c.get_date()
        date_totals[d] = date_totals.get(d, 0) + c.get_calories()

    table = Table(title="Calorie Breakdown by Date", box=box.SIMPLE_HEAVY)
    table.add_column("Date", style="magenta")
    table.add_column("Calories", style="yellow")
    for d, cal in date_totals.items():
        table.add_row(str(d), str(cal))
    console.print(table)
