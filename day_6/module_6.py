# Day 6: 30 Days of Python Programming - Dictionary Exercises

# 1. Create an empty dictionary called dog
dog = {}
print(dog)  # Output: {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3
print(dog)  
# Output: {'name': 'Buddy', 'color': 'Brown', 'breed': 'Labrador', 'legs': 4, 'age': 3}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "country": "USA",
    "city": "New York",
    "address": "1234 Elm Street"
}
print(student)
# Output: student dictionary with specified keys and values

# 4. Get the length of the student dictionary
length_of_student = len(student)
print(length_of_student)  # Output: 9 (number of keys in the dictionary)

# 5. Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print(skills)  # Output: ['Python', 'Data Analysis', 'Machine Learning']
print(type(skills))  # Output: <class 'list'>

# 6. Modify the skills values by adding one or two skills
student["skills"].append("Web Development")
student["skills"].append("Cloud Computing")
print(student["skills"])  
# Output: ['Python', 'Data Analysis', 'Machine Learning', 'Web Development', 'Cloud Computing']

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)  # Output: ['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city', 'address']

# 8. Get the dictionary values as a list
values_list = list(student.values())
print(values_list)  
# Output: ['John', 'Doe', 'Male', 21, 'Single', ['Python', 'Data Analysis', 'Machine Learning', 'Web Development', 'Cloud Computing'], 'USA', 'New York', '1234 Elm Street']

# 9. Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print(items_list)
# Output: 
# [
# ('first_name', 'Umar'),
# ('last_name', 'Musa'),
# ('gender', 'Male'),
# ('age', 21),
# ('marital_status', 'Single'),
# ('skills', ['Python', 'Data Analysis', 'Machine Learning', 'Web Development', 'Cloud Computing']),
# ('country', 'Nigeria'),
# ('city', 'Kano'),
# ('address', '1357 hotoro')
# ]

# 10. Delete one of the items in the dictionary
del student["address"]
print(student)  
# Output: 'address' key is removed from the dictionary

# 11. Delete the student dictionary
del student
# print(student)  # This will raise an error because the dictionary has been deleted
