from workout.user_input import get_workout_from_user
from workout.storage import save_workouts_to_json, load_workouts_from_json

FILENAME = "data/workouts.json"

def main():
    print("----Welcome to FitTrack-----")

    workouts = load_workouts_from_json(FILENAME)
    print(f"📜 Loaded {len(workouts)} workouts.")

    while True:
        print("\nWhat would you like to do?")
        print("1 - Add Workout")
        print("2 - List Workouts")
        print("3 - Quit")
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
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
