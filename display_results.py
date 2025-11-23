from get_inputs import get_inputs
def display_results(bmi, score, risk_level):
    print("\n=== RESULT ===")
    print(f"Your BMI: {bmi:.2f}")
    print(f"Diabetes Risk Score: {score}")
    print(f"Risk Level: {risk_level}")


def diabetes_risk_calculator():
    # Step 1: Get user inputs
    age, weight, height, bp, glucose, family_history, activity = get_inputs()

    # Step 2: Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Step 3: Calculate total risk score
    score = calculate_score(age, bmi, bp, glucose, family_history, activity)

    # Step 4: Determine risk level
    risk_level = determine_risk_level(score)

    # Step 5: Display final results
    display_results(bmi, score, risk_level)


# Run the modular program
diabetes_risk_calculator()