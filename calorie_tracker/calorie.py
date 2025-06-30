from datetime import date

class CalorieTracker:
    def __init__(self , meal_name: str , calories: int, date: date):
        self.__meal_name = meal_name
        self.__calories = calories
        self.__date = date
        
        def get_meal_name(self):
            return self.__meal_name
        def get_calories(self):
            return self.__calories
        def get_date(self):
            return self.__date
        def to_dict(self):
            return {
                "meal_name": self.__meal_name,
                "calories": self.__calories,
                "date": self.__date
            }

