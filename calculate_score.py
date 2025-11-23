def calculate_score(age, bmi, bp, glucose, family_history, activity):
    score = 0
    
    # Age
    if age > 45:
        score += 2
    elif age > 30:
        score += 1
    
    # BMI
    if bmi >= 30:
        score += 3
    elif bmi >= 25:
        score += 2
    else:
        score += 1
    
    # Blood pressure
    if bp > 140:
        score += 3
    elif bp > 120:
        score += 2
    else:
        score += 1
    
    # Glucose
    if glucose >= 126:
        score += 4
    elif glucose >= 100:
        score += 2
    else:
        score += 1
     
    # Family history
    if family_history == "yes":
        score += 3
    
    # Physical activity
    if activity == "no":
        score += 2
    
    return score