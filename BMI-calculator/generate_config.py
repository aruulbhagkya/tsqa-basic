from configparser import ConfigParser
# CREATE OBJECT
config_file = ConfigParser()

# ADD SECTION
config_file.add_section("male")
config_file.add_section("female")
# ADD SETTINGS TO SECTION
config_file.set("male", "c", "88.362")
config_file.set("male", "d", "13.397")
config_file.set("male", "e", "4.799")
config_file.set("male", "f", "5.677")
config_file.set("female", "g", "447.593")
config_file.set("female", "h", "9.247")
config_file.set("female", "i", "3.098")
config_file.set("female", "j", "4.330")

# SAVE CONFIG FILE
with open(r"bmr.ini", 'w') as file:
 config_file.write(file)


