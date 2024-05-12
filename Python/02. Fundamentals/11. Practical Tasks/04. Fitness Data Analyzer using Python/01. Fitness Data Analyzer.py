def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    # Complete the implementation of this function
    pass

def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    # Complete the implementation of this function
    pass

def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    # Fix and complete the implementation of this function
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people

# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")

