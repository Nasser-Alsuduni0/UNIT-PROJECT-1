from datetime import date

class Workout:
    def __init__(self, workout_type: str, workout_duration: int, workout_date: date , km_run :int , sets:int):
        self.__workout_type = workout_type
        self.__workout_duration = workout_duration
        self.__workout_date = workout_date
        self.__km_run = km_run
        self.__sets = sets

    def get_workout_type(self):
        return self.__workout_type

    def get_workout_duration(self):
        return self.__workout_duration

    def get_workout_date(self):
        return self.__workout_date
    
    def get_km_run(self):
        return self.__km_run
    
    def get_sets(self):
        return self.__sets

    def to_dict(self):
        return {
            "workout_type": self.__workout_type,
            "workout_duration": self.__workout_duration,
            "workout_date": str(self.__workout_date) ,
            "kilometers run": self.__km_run ,
            "sets": self.__sets

        }

    

    


            

        




        