height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight in (kg): "))

bmi=weight/(height*height)

print(f"Your Body Mass Index (BMI) is: {bmi: .3f}")