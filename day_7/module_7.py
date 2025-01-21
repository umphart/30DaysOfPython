# Conditionals Exercises: Level 1

# 1. Get user input for age and provide feedback on whether the user is old enough to drive or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")

# 2. Compare my age and your age using if...else and nested conditions to print year or years based on the difference
my_age = 25
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print(f"You are {age_diff} year younger than me.")
    else:
        print(f"You are {age_diff} years younger than me.")
elif my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print(f"I am {age_diff} year younger than you.")
    else:
        print(f"I am {age_diff} years younger than you.")
else:
    print("We are the same age.")

# 3. Compare two numbers using user input and determine which is greater, smaller, or if they are equal
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Conditionals Exercises: Level 2

# 1. Grade students based on their scores
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score!")

# 2. Check the season based on the month input
month = input("Enter a month (e.g., January): ").lower()

if month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif month in ["december", "january", "february"]:
    print("The season is Winter.")
elif month in ["march", "april", "may"]:
    print("The season is Spring.")
elif month in ["june", "july", "august"]:
    print("The season is Summer.")
else:
    print("Invalid month!")

# 3. Add a fruit to the list if it doesn't exist
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit name: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Modified fruit list:", fruits)

# Conditionals Exercises: Level 3

# 1. Check if the person dictionary has a skills key and print out the middle skill
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]  # To find the middle skill
    print(f"The middle skill is: {middle_skill}")

# 2. Check if the person has 'Python' skill and print the result
if 'skills' in person and 'Python' in person['skills']:
    print("The person has Python skill.")
else:
    print("The person doesn't have Python skill.")

# 3. Check the job title based on the skills in the skills list
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. If the person is married and lives in Finland, print personal info
if person['is_married'] and person['country'].lower() == 'finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
