# Task 1: Declare age as integer variable
age = 25  # Example age (you can modify this)

# Task 2: Declare height as a float variable
height = 5.9  # Example height in meters

# Task 3: Declare a variable that stores a complex number
complex_number = 3 + 4j  # Example complex number

# Task 4: Calculate area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print(f"The area of the triangle is {area_of_triangle}")

# Task 5: Calculate perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter_of_triangle}")

# Task 6: Calculate area and perimeter of a rectangle
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_of_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_of_rectangle}")

# Task 7: Calculate area and circumference of a circle
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius
print(f"The area of the circle is {area_of_circle}")
print(f"The circumference of the circle is {circumference_of_circle}")

# Task 8: Calculate slope, x-intercept, and y-intercept of y = 2x - 2
# Let's assume two points for the slope calculation
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print(f"Slope of the line is {slope}")

# Task 9: Calculate Euclidean distance between points (2,2) and (6,10)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Euclidean distance between (2, 2) and (6, 10) is {distance}")

# Task 10: Compare slopes of tasks 8 and 9
# Since slope is related to the line, it’s not comparable directly with distance, but let's show a comparison
print(f"Are the slope and distance equal? {slope == distance}")

# Task 11: Calculate the value of y = x^2 + 6x + 9
x_value = float(input("Enter the value of x: "))
y_value = x_value ** 2 + 6 * x_value + 9
print(f"The value of y is {y_value}")

# Task 12: Find the length of 'python' and 'dragon', make a falsy comparison
python_length = len("python")
dragon_length = len("dragon")
print(f"Is the length of 'python' equal to the length of 'dragon'? {python_length == dragon_length}")

# Task 13: Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print(f"Is 'on' found in both 'python' and 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")

# Task 14: Use 'in' operator to check if 'jargon' is in a sentence
sentence = "I hope this course is not full of jargon."
print(f"Is 'jargon' in the sentence? {'jargon' in sentence}")

# Task 15: Find the length of 'python' and convert it to float, then to string
python_len = len("python")
float_len = float(python_len)
str_len = str(float_len)
print(f"Length of 'python' as float: {float_len} and as string: {str_len}")

# Task 16: Check if a number is even
number = int(input("Enter a number to check if it's even: "))
is_even = number % 2 == 0
print(f"Is the number even? {is_even}")

# Task 17: Check if floor division of 7 by 3 is equal to int('2.7')
print(f"Is the floor division of 7 by 3 equal to int('2.7')? {7 // 3 == int(2.7)}")

# Task 18: Check if the type of '10' is equal to the type of 10
print(f"Is type of '10' equal to type of 10? {type('10') == type(10)}")

# Task 19: Check if int('9.8') is equal to 10
print(f"Is int('9.8') equal to 10? {int(9.8) == 10}")

# Task 20: Calculate pay based on hours and rate per hour
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print(f"Your weekly earning is {pay}")

# Task 21: Calculate the number of seconds a person can live based on years
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds.")

# Task 22: Display a table
print("Displaying the table:")
for i in range(1, 6):
    print(f"{i} {i**1} {i**2} {i**3} {i**4}")
