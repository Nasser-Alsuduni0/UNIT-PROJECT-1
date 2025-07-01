import json
from .workout import Workout

def save_workouts_to_json(workouts, filename):
    data = [w.to_dict() for w in workouts]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(workouts)} workouts to {filename}")

def load_workouts_from_json(filename):
    workouts = []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
             workouts.append(Workout.from_dict(item))

    except FileNotFoundError:
        print("No saved workouts yet.")
    except json.JSONDecodeError:
        print("JSON file is empty or invalid.")
    return workouts
