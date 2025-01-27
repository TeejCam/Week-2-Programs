# BMI = mass(kg) / height (m)^2 = mass(lb) / height (in) ^ 2 703

def BMI(feet, inches, weight):
    height = (feet*12) + inches
    BMI = (weight/(height**2)) * 703
    return round(BMI, 1)

userFeet = float(input("Enter feet component of your height: "))
userInches = float(input("Now enter the inches component: "))
userWeight = float(input("Enter weight in pounds: "))

userBMI = BMI(userFeet, userInches, userWeight)

print("Your BMI is: " + str(userBMI) + " kg/m^2")

print("According to the World Health Organization, the BMI categories in kg/m^2 are as follows:")
print("Underweight (severe thinness): <16.0")
print("Underweight (moderate thinness): 16.0-16.9")
print("Underweight (mild thinness): 17.0-18.4")
print("Normal range: 18.5-24.9")
print("Overweight (pre-obese): 25.0-29.9")
print("Obese (class 1): 30.0-34.9")
print("Obese (class 2): 35.0-39.9")
print("Obese (class 3): ≥ 40.0")