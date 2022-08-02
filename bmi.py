import os
import csv

def get_input_to_calculate_bmi():
    "This function gets the input from the user"
        print("Enter the weight of the user in Kg's")
        # function get the weight of user
        weight_of_the_user = float(input())
           
    "This function gets the input from user"
        print("Enter the height of the user in cm")
        # Get the height of the user through keyboard
            height_of_the_user = float(input())
            
def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the bmi"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/(height_of_the_user/100)**2)

    # Return the BMI of the user to the called function
    return bmi_of_the_user

def check_user_bmi_category(bmi):
    "This function checks if the user is underweight, normal, overweight or obese"    
    if bmi <= 18.5:
         print("The user is considered as underweight")
    elif bmi > 18.5 and bmi < 24.9:
         print("The user is considered as normal weight")
    elif bmi > 25 and bmi <= 29.9:
        print("The user is considered as overweight")
    elif bmi >=30:
        print("The user is considered as obese")

def compare_user_bmi_with_celebrity_csv(bmi_of_the_user):
    "This functions reads the csv file and compare the BMI value with celebrity and returns the celebrity name"
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data',"celebrity.csv"))
    matched_celebrity = []
    with open(filename,"r") as fp:
        csv_file = csv.reader(fp)
        next(csv_file)
        for i, row in enumerate(csv_file):
            bmi_value_in_row = row[3]
            player_name = row[0]    
            if float(bmi_value_in_row) == bmi_of_the_user:
                matched_celebrity.append({player_name:bmi_value_in_row})
    if not matched_celebrity:
        print("No matching data")
    else:
        print("Your BMI is matching with")
        print ("matched_celebrity")
    
# Program starts here
if __name__ == "__main__":
    # This calling function gets the input from the user
    weight_of_the_user,height_of_the_user = get_input_to_calculate_bmi()     
    
    # This calling function calculates the BMI of the user
    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)
    print("BMI of the user is :",bmi_value)
# This function is used to calculate the user's criteria
    check_user_bmi_category(bmi_value)
# This function is used to read the CSV file and compare the BMI value
    compare_user_bmi_with_celebrity_csv(bmi_value)
