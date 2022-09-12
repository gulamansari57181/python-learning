height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight in (kg): "))

bmi=weight/(height*height)

print(f"Your Body Mass Index (BMI) is: {bmi: .3f}")

if bmi <= 18.5:
    print(f"Eat some food budddy. Right now you are 'underweight' with bmi: {bmi: .3f}")
elif bmi <= 25:
     print(f"Congrats.Right now you have 'normal weight' with bmi: {bmi: .3f}")
elif bmi <= 30:
     print(f"Focus on your diet buddy. Right now you are 'overweight' with bmi: {bmi: .3f}")
elif bmi <= 35:
     print(f"Sign of warning. Right now you are 'obese' with bmi: {bmi: .3f}")
else:
     print(f"Warning!! You should take medical treatment.Right now you are 'clinically obese' with bmi: {bmi: .3f}")
    
    

