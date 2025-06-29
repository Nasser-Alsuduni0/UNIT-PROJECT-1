from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich import box


console = Console()

def show_workout_summary(workouts):
    
    total_km = sum(float(w.get_km_run() or 0) for w in workouts)
    total_duration = sum(w.get_workout_duration() or 0 for w in workouts)
    total_sets = sum(w.get_sets() or 0 for w in workouts)

    console.print("\n[bold green]=== Workout Summary ===[/bold green]")
    console.print(f"[cyan]Total KM Run:[/cyan] {total_km:.2f} km")
    console.print(f"[cyan]Total Duration:[/cyan] {total_duration} minutes")
    console.print(f"[cyan]Total Sets:[/cyan] {total_sets} sets\n")

    type_counts = {}
    for w in workouts:
        t = w.get_workout_type()
        type_counts[t] = type_counts.get(t, 0) + 1

    table = Table(title="Workout Type Breakdown", box=box.SIMPLE_HEAVY)
    table.add_column("Workout Type", style="magenta")
    table.add_column("Count", style="yellow")

    for workout_type, count in type_counts.items():
        table.add_row(workout_type, str(count))

    console.print(table)

