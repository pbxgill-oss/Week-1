class BMI:
   def calculate_bmi(self, weight, height):
      bmi = weight/ height**2
      return bmi

   def bmi_category(self, bmi):
      if bmi < 18.5:
         return "underweight"
      elif bmi <24.9:
         return "normal weight"
      elif bmi <29.9:
         return "overwight"
      else:
         return "obese"

obj = BMI()
weight = float(input("enter your weight in kg :"))
height = float(input("enter your height in meters :"))

bmi = obj.calculate_bmi(weight, height)

print("BMI:", round(bmi, 2))
print("Category:", obj.bmi_category(bmi))

      

       
   