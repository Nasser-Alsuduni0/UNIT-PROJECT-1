from workout_tracker.user_input import get_workout_from_user
from workout_tracker.storage import save_workouts_to_json, load_workouts_from_json
from workout_tracker.analytics import show_workout_summary
from calorie_tracker.user_input import get_meal_from_user
from calorie_tracker.storage import save_calories_to_json, load_calories_from_json
from calorie_tracker.analytics import show_calorie_summary
from calorie_tracker.calorie import CalorieTracker
from rich.table import Table
from rich.console import Console
from rich import box
from profile import create_user_profile
from goals import save_goals, load_goals, set_goals, show_progress


FILENAME = "data/workouts.json"


def workout_tracker_menu():
    print("\n---- Welcome to FitTrack ----")

    workouts = load_workouts_from_json(FILENAME)
    print(f"Loaded {len(workouts)} workouts.")

    while True:
        print("\nWhat would you like to do?")
        print("1 - Add Workout")
        print("2 - List Workouts")
        print("3 - View Analytics")
        print("4 - Return to Main Menu")
        choice = input("> ").strip()

        if choice == "1":
            workout = get_workout_from_user()
            if workout:
                workouts.append(workout)
                save_workouts_to_json(workouts, FILENAME)
        elif choice == "2":
            if not workouts:
                print("No workouts recorded yet.")
            else:
                table = Table(title="Workout Entries", box=box.SIMPLE_HEAVY)
                table.add_column("Type", style="magenta")
                table.add_column("Duration (min)", style="yellow")
                table.add_column("Date", style="cyan")
                table.add_column("KM Run", style="green")
                table.add_column("Sets", style="blue")
                for w in workouts:
                    d = w.to_dict()
                    table.add_row(
                        str(d["workout_type"]),
                        str(d["workout_duration"]),
                        str(d["workout_date"]),
                        str(d["kilometers run"]),
                        str(d["sets"])
                    )
                Console().print(table)
        elif choice == "3":
            if not workouts:
                print("No workouts recorded yet.")
            else:
                show_workout_summary(workouts)
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def calorie_tracker_menu():
    print("\n---- Welcome to Calorie Tracker ----")

    calories = load_calories_from_json("data/calories.json")
    print(f"Loaded {len(calories)} calorie entries.")

    while True:
        print("\nWhat would you like to do?")
        print("1 - Add Meal Entry")
        print("2 - List Meals")
        print("3 - View Analytics")
        print("4 - Return to Main Menu")
        choice = input("> ").strip()

        if choice == "1":
            while True:
                meal = get_meal_from_user()
                if meal:
                    calories.append(meal)
                    save_calories_to_json(calories, "data/calories.json")
                    print("Calorie entry added.")
                else:
                    print("No valid entry provided.")
                if input("Add another meal? (y/n): ").strip().lower() != 'y':
                    break
        elif choice == "2":
            if not calories:
                print("No meals recorded yet.")
            else:
                table = Table(title="Meal Entries", box=box.SIMPLE_HEAVY)
                table.add_column("Meal Name", style="magenta")
                table.add_column("Calories", style="yellow")
                table.add_column("Date", style="cyan")
                for c in calories:
                    d = c.to_dict()
                    table.add_row(str(d["meal_name"]), str(
                        d["calories"]), str(d["date"]))
                Console().print(table)
        elif choice == "3":
            if not calories:
                print("No meals recorded yet.")
            else:
                show_calorie_summary(calories)
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


def main():
    user_profile = create_user_profile()
    goals = load_goals()
    while True:
        print("\n===== Welcome to FitTrack =====")
        print("1 - Workout Tracker")
        print("2 - Calorie Tracker")
        print("3 - Goals & Progress")
        print("4 - Quit")
        choice = input("> ").strip()

        if choice == "1":
            workout_tracker_menu()
        elif choice == "2":
            calorie_tracker_menu()
        elif choice == "3":
            print("\n--- Goals & Progress ---")
            if not goals:
                goals = set_goals(user_profile)
            show_progress(user_profile, goals,
                          load_calories_from_json, load_workouts_from_json)
            if input("Do you want to update your goals? (y/n): ").strip().lower() == 'y':
                goals = set_goals(user_profile)
        elif choice == "4":
            print(f"Goodbye, {user_profile['name']}!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
