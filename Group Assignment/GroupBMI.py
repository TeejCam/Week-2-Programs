#This program was made by Jerome, Adi, and Hatice

#first prompt user
print("Hello! I will ask you to enter your weight in pounds and height in feet and inches.")

#this function and its variables follows the lowerCamelCase convention we chose
def userWeightAndHeight():
    weight = float(input("Please enter your weight in pounds: "))
    heightFt = float(input("Please enter your height in feet: "))
    heightIn = float(input("Please enter your height in inches: "))
    heightTotal = (heightFt * 12) + heightIn
    return weight, heightTotal

#BMI is a commonly used acronym, so we are using it, because the full name would be too long
def calculateBMI(pounds, inches):
    BMI = (pounds / (inches*inches)) * 703
    print("BMI: ", f"{BMI:.1f}")

#our function and variable names are concise and to the point
def displayRange():
    print("Underweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")

#call functions
weight, heightTotal = userWeightAndHeight()
calculateBMI(weight, heightTotal)
displayRange()