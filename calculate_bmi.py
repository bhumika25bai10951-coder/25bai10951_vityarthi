def calculate_bmi(weight, height):
    # Convert height to meters for correct BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi