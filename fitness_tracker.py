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
        self.goals = {
            "calories_goal": 0,
            "workouts_goal": 0,
            "duration_goal": 0
        }
    
    def set_calories_goal(self, calories):
        self.goals['calories_goal'] = calories
    
    def set_workouts_goal(self, workouts):
        self.goals['workouts_goal'] = workouts
    
    def set_duration_goal(self, duration):
        self.goals['duration_goal'] = duration

    def create_workout_plan(self, workout):
        self.workouts.append(workout)

    def track_progress(self):
        total_calories_burned = 0
        total_workouts_completed = len(self.workouts)
        total_duration = 0

        for workout in self.workouts:
            total_calories_burned += workout.total_calories_burned()

            for exercise in workout.exercises:
                total_duration += exercise['duration']

        if total_calories_burned >= self.goals['calories_goal']:
            print(f"Congratulations, {self.name}! You have achieved your calories goal")
        
        if total_workouts_completed >= self.goals['workouts_goal']:
            print(f"Congratulations, {self.name}! You have achieved your workouts goal")
        
        if total_duration >= self.goals['duration_goal']:
            print(f"Congratulations, {self.name}! You have achieved your duration goal")

        return total_calories_burned, total_workouts_completed, total_duration


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

user1.set_calories_goal(300)
user1.set_workouts_goal(5)
user1.set_duration_goal(120)

# Tracking progress
calories_burned, workouts_completed, total_duration = user1.track_progress()
print(f"{user1.name} has burned {calories_burned} calories, completed {workouts_completed} workouts, "
      f"and exercised for a total duration of {total_duration} minutes.")
