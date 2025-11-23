# 25bai10951_vityarthi
# Diabetes Risk Calculator

#overview

Diabetes Risk Calculator is a simple Python console application that estimates a person's diabetes risk level (LOW, MODERATE, or HIGH) using basic health information.  
The program asks for age, weight, height, blood pressure, fasting glucose, family history of diabetes, and physical activity, then calculates a score and risk level based on predefined rules.

#Features

- Takes user inputs for:
  - Age
  - Weight (kg)
  - Height (cm)
  - Systolic blood pressure
  - Fasting glucose (mg/dL)
  - Family history of diabetes (yes/no)
  - Physical activity (yes/no)
- Calculates Body Mass Index (BMI).
- Computes a total diabetes risk score using if–else conditions.
- Classifies the result as LOW, MODERATE, or HIGH risk.
- Displays BMI, score, and final risk level in a clear format.

 #Technologies / Tools Used

- Python 3.x
- Standard Python input/output (input(), print())
- Basic control structures (functions, if–elif–else, arithmetic expressions)

 #Installation and How to Run

1. Install Python**  
   Make sure Python 3 is installed on your system.

2. Download or create project files**  
   Example (single-file version):
   - diabetes_risk_calculator.py
   or (modular version):
   - get_inputs.py
   - calculate_bmi.py
   - calculate_score.py
   - determine_risk_level.py
   - display_results.py
   - main.py

3. Open a terminal / command prompt in the project folder.**

4. Run the program:

   - If everything is in one file:
     
     python diabetes_risk_calculator.py
     
   - If you use modules and a main file:
     
     python main.py
     

5. Follow the on-screen instructions**  
   Enter numeric values when asked for age, weight, height, blood pressure, and glucose, and type 'yes' or 'no' for the yes/no questions.

#Instructions for Testing

- Functional testing**
  - Enter normal values:
    - Age: 25, BMI in normal range, normal blood pressure and glucose, active, no family history.  
      - Expect: relatively LOW score and LOW risk.
  - Enter higher-risk values:
    - Age: 50, BMI ≥ 30, high blood pressure (>140), high glucose (≥126), family history 'yes', activity 'no'.  
      - Expect: higher score and HIGH risk.

  -Boundary testing**
  - Try ages around 30 and 45 to see score changes (e.g., 29, 31, 45, 46).
  - Try BMI values around 25 and 30 to see point differences.
  - Try glucose values just below 100, between 100–125, and ≥126.

  - Input robustness (manual)**
  - Observe what happens if you accidentally type letters when a number is requested.  
    (You can later improve the code by adding 'try/except' to handle invalid inputs.)

#Screenshots (Optional)

You can add screenshots of your program running in the terminal. For example:

<img width="1192" height="461" alt="image" src="https://github.com/user-attachments/assets/6d0280ea-1949-4f59-bf0f-97f43b03c856" />
