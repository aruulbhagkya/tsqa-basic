import os 
import csv 
class BMI():

    #Defining the initiating the method
    def __init__(self ,weight ,height):
        self.weight = weight
        self.height = height

#Calculating BMI
    def calculate_BMI(self):
        return (int(self.weight/(self.height/100)**2))

#Weight input
weight=int(input("Enter the weight in kg : "))
#Height input
height=int(input("Enter the weight in cenimeter : "))

obj = BMI(weight,height)
x= obj.calculate_BMI()
print("BMI of user is : ",x)

 
if x <= 18.5:
     print("The user is considered as underweight")
elif x > 18.5 and x < 24.9:
         print("The user is considered as normal weight")
elif x > 25 and x <= 29.9:
        print("The user is considered as overweight")
elif x>=30:
        print("The user is considered as obese")

filename = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data',"celebrity.csv"))
matched_celebrity = []
with open(filename,"r") as fp:
        csv_file = csv.reader(fp)
        next(csv_file)
        for i, row in enumerate(csv_file):
            bmi_value_in_row = row[3]
            celebrity_name = row[0]    
            if int(bmi_value_in_row) == x:
                matched_celebrity.append({celebrity_name})
if not matched_celebrity:
        print("No matching data")
else:
        print("Your BMI is matching with:",matched_celebrity)

   
   