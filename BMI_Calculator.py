# take weight & height from the user as input
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Formula to calculate BMI
bmi = round(weight / (height ** 2))

# conditional statements
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print("Your BMI is 33, you are obese.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print("Your BMI is 33, you are obese.")
else:
    print("Your BMI is 40, you are clinically obese.")