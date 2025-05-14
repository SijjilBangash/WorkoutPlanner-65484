def calculate_bmi(weight, height):
    # Height is converted from cm to meters
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def workout_and_diet_suggestion(bmi):
    if bmi < 18.5:
        return "Underweight", "Workout: 20 mins light exercise\nDiet: High-protein, high-calorie meals"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "Workout: 30 mins moderate exercise\nDiet: Balanced meals with fruits and vegetables"
    elif 25 <= bmi < 30:
        return "Overweight", "Workout: 45 mins cardio + strength training\nDiet: Low-carb, more fiber and protein"
    else:
        return "Obese", "Workout: 60 mins daily, focus on cardio\nDiet: Consult a dietitian, reduce sugar and fat"

def workout_planner():
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()

        # Check for empty fields
        if not weight_input or not height_input:
            raise ValueError("Fields cannot be empty.")

        # Convert inputs to float
        weight = float(weight_input)
        height = float(height_input)

        # Check for negative or zero values
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category, suggestion = workout_and_diet_suggestion(bmi)

        print(f"\nYour BMI is: {bmi:.2f} ({category})")
        print("Suggestions:")
        print(suggestion)

    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)


workout_planner()
