def get_inputs():
    print("=== Diabetes Risk Calculator ===\n")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (centimeters): "))
    bp = int(input("Enter your systolic blood pressure: "))
    glucose = int(input("Enter your fasting glucose (mg/dL): "))
    family_history = input("Family history of diabetes? (yes/no): ").strip().lower()
    activity = input("Are you physically active? (yes/no): ").strip().lower()
    
    return age, weight, height, bp, glucose, family_history, activity