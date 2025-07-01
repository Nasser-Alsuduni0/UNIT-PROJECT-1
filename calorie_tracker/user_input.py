from datetime import date
from .calorie import CalorieTracker  

def get_meal_from_user():
    while True: 
        meal_name = input("Enter the meal name: ").strip()
        if meal_name.isalpha():
            break
        else:
            print("Please enter only alphabetical characters for the meal name.")

    while True:
        calories = input("Enter how many calories it has: ").strip()
        if calories.isdigit():
            calories = int(calories)
            break
        else:
            print("Please enter a valid number for calories.")

    today = str(date.today())
    return CalorieTracker(meal_name, calories, today)




