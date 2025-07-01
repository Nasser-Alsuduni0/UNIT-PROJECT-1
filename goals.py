import json
import os
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime, timedelta


def save_goals(goals, filename="data/goals.json"):
    with open(filename, 'w') as f:
        json.dump(goals, f, indent=2)


def load_goals(filename="data/goals.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as f:
        return json.load(f)


def set_goals(user_profile):
    console = Console()
    console.print("[bold green]Set your fitness goals![/bold green]")
    target_weight = input(f"Enter your target weight (kg) [current: {user_profile['weight']}]: ").strip()

    try:
        target_weight = float(target_weight)
    except ValueError:
        target_weight = user_profile['weight']
    weekly_workout_goal = input(
        "Enter your weekly workout goal (number of workouts): ").strip()
    try:
        weekly_workout_goal = int(weekly_workout_goal)
    except ValueError:
        weekly_workout_goal = 3
    daily_calorie_limit = input("Enter your daily calorie limit: ").strip()
    try:
        daily_calorie_limit = int(daily_calorie_limit)
    except ValueError:
        daily_calorie_limit = 2000
    goals = {
        "target_weight": target_weight,
        "weekly_workout_goal": weekly_workout_goal,
        "daily_calorie_limit": daily_calorie_limit
    }
    save_goals(goals)
    console.print("[bold cyan]Goals saved![/bold cyan]")
    return goals


def show_progress(user_profile, goals, load_calories_from_json, load_workouts_from_json):
    console = Console()
    calories = load_calories_from_json("data/calories.json")
    workouts = load_workouts_from_json("data/workouts.json")
    
    weight_progress = user_profile['weight'] - \
        goals.get('target_weight', user_profile['weight'])
    
    today = datetime.today().date()
    week_ago = today - timedelta(days=7)
    workouts_this_week = [
        w for w in workouts if w.get_workout_date() >= str(week_ago)]
   
    calories_today = sum(c.get_calories()
                         for c in calories if c.get_date() == str(today))
    table = Table(title="Your Progress", box=box.SIMPLE_HEAVY)
    table.add_column("Goal", style="magenta")
    table.add_column("Current", style="yellow")
    table.add_column("Target", style="green")
    table.add_column("Progress", style="cyan")
    table.add_row("Weight (kg)", f"{user_profile['weight']}",f"{goals.get('target_weight', '-')}", f"{abs(weight_progress):.1f} to go")
    table.add_row("Workouts (this week)", f"{len(workouts_this_week)}", f"{goals.get('weekly_workout_goal', '-')} per week",
                  f"{len(workouts_this_week)}/{goals.get('weekly_workout_goal', '-')} done")
    table.add_row("Calories (today)", f"{calories_today}", f"{goals.get('daily_calorie_limit', '-')} per day",
                  f"{calories_today}/{goals.get('daily_calorie_limit', '-')} used")
    console.print(table)
