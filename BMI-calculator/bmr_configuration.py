""" We will use Python scripts for absolute beginners
 This script shows the use of BMR Calculator = Basal Metabolic Rate Calculator.
 BMR gives the value of the calories which the body intakes during weight gain or weight loss.
 The BMR Calculator:
    # Get the Age of the user
    # Get the Gender of the user
    # Get the weight(Kg) of the user
    # Get the height(cm) of the user
    # Calculate the BMI using the formula on the basis of gender, age, height and weight
       For Male: BMR= 88.362+(13.397*weight in kg/lb)+(4.799*height in cm/in")- (5.677*age in years)
       For Female: BMR = 447.593+(9.247*weight in kg/ib)+(3.098*height in cm/in")- (4.330*age in years)
       

Exercise 1: Calculate the BMR (in calorie)
Exercise 2: Creating Configuration file for BMR

from configparser import ConfigParser


print("*****Welcome To The BMR Calculator*****")
def __getinput_to_calculate_bmr():
    "This function gets the input from the user "
    print("Enter Weight in kg and Height in cm")
    Weight_of_the_user = float(input())
    Height_of_the_user = float(input())
    Gender_of_the_user = (input("Enter the gender of the user M/F:"))
    Age_of_the_user = float(input("Enter the age of the user:"))

    return Weight_of_the_user, Height_of_the_user, Age_of_the_user, Gender_of_the_user

def calculate_bmr (Weight_of_the_user, Height_of_the_user, Age_of_the_user,Gender_of_the_user):



    config_file = ConfigParser()
    config_file.read("bmr.ini")
    x = config_file["male"]
    a=float(x["c"])
    b=float(x["d"])
    c=float(x["e"])
    d=float(x["f"])
    y = config_file["female"]
    e=float(y["g"])
    f=float(y["h"])
    g=float(y["i"])
    h=float(y["j"])

    # Here if the Gender_of_the_user is 'M' i.e Male, then formula will be BMR_Male
    if Gender_of_the_user.upper() == 'M' :
    
         BMR_Male = round((a + (b * Weight_of_the_user) + (c * Height_of_the_user)- (d*Age_of_the_user)),2)
    elif Gender_of_the_user == 'Female':
         BMR_Male = round((e + (f * Weight_of_the_user*2.2) + (g* Height_of_the_user*39.37) - (h * Age_of_the_user)),2)
    return BMR_Male


if __name__ == "__main__":
    # This calling function gets the input from the user
    weight_of_the_user, height_of_the_user, Gender_of_the_user, age_of_the_user = __getinput_to_calculate_bmr()

    # This calling function stores the BMI of the user
    BMR_value = calculate_bmr(weight_of_the_user, height_of_the_user, Gender_of_the_user,age_of_the_user)

    print("BMR of the user is :", BMR_value )

    


