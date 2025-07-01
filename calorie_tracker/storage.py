import json
from .calorie import CalorieTracker

def save_calories_to_json(calories, filename):
    data = [c.to_dict() for c in calories]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(calories)} calorie entries to {filename}")  

def load_calories_from_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [CalorieTracker.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"No calorie data found at {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}")
        return []