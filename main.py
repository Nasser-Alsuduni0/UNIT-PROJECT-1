from workout.user_input import get_workout_from_user
from workout.storage import save_workouts_to_json, load_workouts_from_json
from workout.analytics import show_workout_summary


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
                for w in workouts:
                    print(w.to_dict())

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
    print("This feature is coming soon!")
    input("Press Enter to return to main menu.")


def main():
    while True:
        print("\n===== Welcome to FitTrack =====")
        print("1 - Workout Tracker")
        print("2 - Calorie Tracker")
        print("3 - Quit")
        choice = input("> ").strip()

        if choice == "1":
            workout_tracker_menu()
        elif choice == "2":
            calorie_tracker_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
