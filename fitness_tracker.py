class Exercise:
    def __init__(self, name, calories_burned_per_minute):
        self.name = name
        self.calories_burned_per_minute = calories_burned_per_minute


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise, duration_minutes):
        routine = {'exercise': exercise, 'duration': duration_minutes}
        self.exercises.append(routine)
    
    def total_calories_burned(self):
        total_calories = 0
        for exercise in self.exercises:
            total_calories += exercise['exercise'].calories_burned_per_minute * exercise['duration']
        return total_calories

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []
    
    def create_workout_plan(self, workout):
        self.workouts.append(workout)

    def track_progress(self):
        total_calories_burned = 0
        for workout in self.workouts:
            total_calories_burned += workout.total_calories_burned()
        return total_calories_burned

    def set_goals(self):
        pass


# Creating exercises
exercise1 = Exercise("Running", 10)
exercise2 = Exercise("Cycling", 8)
exercise3 = Exercise("Jumping Jacks", 12)

# Creating a workout
my_workout = Workout("Morning Workout")
my_workout.add_exercise(exercise1, 30)  # Running for 30 minutes
my_workout.add_exercise(exercise3, 15)  # Jumping Jacks for 15 minutes

# Creating a user
user1 = User("Alice", 30, 150)
user1.create_workout_plan(my_workout)

# Tracking progress
calories_burned = user1.track_progress()
print(f"{user1.name} has burned {calories_burned} calories.")
