from .workout import Workout
from datetime import date

def get_workout_from_user():
    today = date.today()

    while True:
        workout_type_choice = input(
            "Choose your workout number:\n 1 - Running\n 2 - Weightlifting\n  3 - Both> "
        ).strip()

        if workout_type_choice == "1":
            km_run = input("How many kilometers did you run? ").strip()
            duration = int(input("Approximate duration in minutes: ").strip())
            return Workout("Running", duration, today , km_run , None)

        elif workout_type_choice == "2":
            while True:
                lifting_choice = input(
                    "Choose your Weightlifting workout:\n 1 - Deadlift\n 2 - Bench press\n 3 - Dumbbell curl\n> "
                ).strip()

                if lifting_choice == "1":
                    sets = int(input("Enter how many sets: ").strip())
                    return Workout("Deadlift", sets * 5, today , None, sets)

                elif lifting_choice == "2":
                    sets = int(input("Enter how many sets: ").strip())
                    return Workout("Bench press", sets * 5, today , None , sets)

                elif lifting_choice == "3":
                    sets = int(input("Enter how many sets: ").strip())
                    return Workout("Dumbbell curl", sets * 5, today , None , sets)

                else:
        
                    print("Enter a valid number (1, 2, or 3).")
            
        elif workout_type_choice == "3":
            
            km_run =input("How many kilometers did you run? \n > ")
            while True:
                lifting_choice = input(
                    "Choose your Weightlifting workout:\n 1 - Deadlift\n 2 - Bench press\n 3 - Dumbbell curl\n> "
                ).strip()

                if lifting_choice == "1":
                    sets = int(input("Enter how many sets: ").strip())
                    duration_run = int(input("How many minutes it took for the run? \n> ").strip())
                    return Workout("Running and Deadlift", sets * 5 + duration_run, today, km_run , sets)

                elif lifting_choice == "2":
                    sets = int(input("Enter how many sets: ").strip())
                    duration_run = int(input("How many minutes it took for the run? \n> ").strip())
                    return Workout("Running and Bench press", sets * 5 + duration_run, today, km_run , sets)

                elif lifting_choice == "3":
                    sets = int(input("Enter how many sets: ").strip())
                    duration_run = int(input("How many minutes it took for the run? \n> ").strip())
                    return Workout("Running and Dumbbell curls", sets * 5 + duration_run, today, km_run ,sets )

                else:
        
                    print("Enter a valid number (1, 2, or 3).")
            

        else:
            print("Enter a valid number (1 or 2).")

