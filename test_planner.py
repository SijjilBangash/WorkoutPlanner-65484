# test_planner.py

import pytest
from planner import calculate_bmi, workout_and_diet_suggestion

# Test for BMI calculation
def test_calculate_bmi():
    assert round(calculate_bmi(70, 175), 2) == 22.86  # Normal weight
    assert round(calculate_bmi(45, 160), 2) == 17.58  # Underweight
    assert round(calculate_bmi(85, 170), 2) == 29.41  # Overweight
    assert round(calculate_bmi(100, 160), 2) == 39.06  # Obese

# Test for workout and diet recommendation
def test_workout_and_diet_suggestion():
    assert workout_and_diet_suggestion(17)[0] == "Underweight"
    assert workout_and_diet_suggestion(22)[0] == "Normal weight"
    assert workout_and_diet_suggestion(27)[0] == "Overweight"
    assert workout_and_diet_suggestion(32)[0] == "Obese"
