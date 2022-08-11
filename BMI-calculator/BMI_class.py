"""
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise3 :
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes
        in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains celebrity data 
        and compare your BMI with a celebrity.Create class for getting input from the user,calculating BMI and check 
        the user category.While getting input check the value you entered is of correct type if not 
        your program should not get crashed.
       
            i)Get user weight in kg 
            ii)Get user height in centimeter
            iii) Use this formula to calculate the BMI
                    BMI = weight_of_the_user/(height_of_the_user/100)**2)
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese
        # Hint
            i)Create a class to get the input from the user 
            ii)Calculate the BMI
            iii)Check the BMI with celebrity BMI by reading the CSV file and display the  matched celebrity name.

"""
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

calculator= BMI(weight,height)
user_BMI= calculator.calculate_BMI()
print("BMI of user is : ",user_BMI)

 
if user_BMI<= 18.5:
     print("The user is considered as underweight")
elif user_BMI> 18.5 and user_BMI < 24.9:
         print("The user is considered as normal weight")
elif user_BMI > 25 and user_BMI <= 29.9:
        print("The user is considered as overweight")
elif user_BMI>=30:
        print("The user is considered as obese")

filename = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data',"celebrity.csv"))
matched_celebrity = []
with open(filename,"r") as fp:
        csv_file = csv.reader(fp)
        next(csv_file)
        for i, row in enumerate(csv_file):
            bmi_value_in_row = row[3]
            celebrity_name = row[0]    
            if int(bmi_value_in_row) == user_BMI:
                matched_celebrity.append({celebrity_name})
if not matched_celebrity:
        print("No matching data")
else:
        print("Your BMI is matching with:",matched_celebrity)

   
   
