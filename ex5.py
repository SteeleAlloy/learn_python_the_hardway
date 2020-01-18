my_name = 'Ashley Steele'
my_age = 38
my_height_inch = 74 # inches
my_height_cm = my_height_inch * 2.54
my_weight = 250 # lbs
my_weight_kg = my_weight * 0.453592
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Red'


print(f"Let's talk about {my_name}.")
print(f"She's {my_height_inch} inches tall and {my_height_cm} centimeters tall. ")
print(f"She's {my_weight} lbs and {my_weight_kg} kilograms heavy.")
print("Actually, that's not too heavy!")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}. ")
