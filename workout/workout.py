from datetime import date

class Workout:
    def __init__(self, workout_type: str, workout_duration: int, workout_date: date):
        self.__workout_type = workout_type
        self.__workout_duration = workout_duration
        self.__workout_date = workout_date

    def get_workout_type(self):
        return self.__workout_type

    def get_workout_duration(self):
        return self.__workout_duration

    def get_workout_date(self):
        return self.__workout_date

    def to_dict(self):
        return {
            "workout_type": self.__workout_type,
            "workout_duration": self.__workout_duration,
            "workout_date": str(self.__workout_date)
        }

    

    


            

        




        