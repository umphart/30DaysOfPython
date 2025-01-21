# Day 2: 30 Days of Python programming

# Declaring variables
first_name = "Umar"
last_name = "Musa"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Kano"
age = 29
year = 2025
is_married = False
is_true = True
is_light_on = False

# Declaring multiple variables on one line
x, y, z = 10, 20, 30

# Exercises: Level 2
# Check the data type of all your variables
print("Data type of first_name:", type(first_name))
print("Data type of last_name:", type(last_name))
print("Data type of full_name:", type(full_name))
print("Data type of country:", type(country))
print("Data type of city:", type(city))
print("Data type of age:", type(age))
print("Data type of year:", type(year))
print("Data type of is_married:", type(is_married))
print("Data type of is_true:", type(is_true))
print("Data type of is_light_on:", type(is_light_on))
print("Data type of x:", type(x))
print("Data type of y:", type(y))
print("Data type of z:", type(z))

# Using len() to find the length of your first name
first_name_length = len(first_name)
print("Length of first name:", first_name_length)

# Compare the length of your first name and last name
last_name_length = len(last_name)
print("Length of last name:", last_name_length)
print("Is first name longer than last name?", first_name_length > last_name_length)

# Declare num_one and num_two
num_one = 5
num_two = 4

# Perform arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Print the results of arithmetic operations
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Calculate the area and circumference of a circle
radius = 30
area_of_circle = 3.14159 * (radius ** 2)
circum_of_circle = 2 * 3.14159 * radius

print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

# Take radius as user input and calculate the area
user_radius = float(input("Enter the radius of the circle: "))
user_area_of_circle = 3.14159 * (user_radius ** 2)
print("Area of the circle with radius", user_radius, "is:", user_area_of_circle)

# Taking user input for first name, last name, country, and age
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

# Print the user-provided details
print(f"User Details: {user_first_name} {user_last_name}, from {user_country}, Age: {user_age}")

# Run help('keywords') to check for reserved keywords
help('keywords')
