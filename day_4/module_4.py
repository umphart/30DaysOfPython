# Day 4: 30 Days of Python programming

# Task 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to form 'Thirty Days Of Python'
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result = str1 + " " + str2 + " " + str3 + " " + str4
print(result)  # Output: Thirty Days Of Python

# Task 2: Concatenate the string 'Coding', 'For', 'All' to form 'Coding For All'
str5 = 'Coding'
str6 = 'For'
str7 = 'All'
result2 = str5 + " " + str6 + " " + str7
print(result2)  # Output: Coding For All

# Task 3: Declare a variable named 'company' and assign it to an initial value "Coding For All"
company = "Coding For All"

# Task 4: Print the 'company' variable using print()
print(company)  # Output: Coding For All

# Task 5: Print the length of the company string using len() method
print(len(company))  # Output: 15

# Task 6: Change all the characters to uppercase letters using upper() method
print(company.upper())  # Output: CODING FOR ALL

# Task 7: Change all the characters to lowercase letters using lower() method
print(company.lower())  # Output: coding for all

# Task 8: Use capitalize(), title(), and swapcase() methods to format the value of the string 'Coding For All'
print(company.capitalize())  # Output: Coding for all
print(company.title())  # Output: Coding For All
print(company.swapcase())  # Output: cODING fOR aLL

# Task 9: Slice out the first word of 'Coding For All'
print(company[0:6])  # Output: Coding

# Task 10: Check if 'Coding For All' contains the word 'Coding' using index, find, or other methods
print(company.find("Coding"))  # Output: 0 (The word "Coding" starts at index 0)

# Task 11: Replace the word 'coding' in the string 'Coding For All' to 'Python'
print(company.replace("Coding", "Python"))  # Output: Python For All

# Task 12: Change 'Python for Everyone' to 'Python for All' using the replace method
sentence = 'Python for Everyone'
new_sentence = sentence.replace("Everyone", "All")
print(new_sentence)  # Output: Python for All

# Task 13: Split the string 'Coding For All' using space as the separator
words = company.split()
print(words)  # Output: ['Coding', 'For', 'All']

# Task 14: Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(', ')
print(companies_list)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Task 15: What is the character at index 0 in the string 'Coding For All'
print(company[0])  # Output: C

# Task 16: What is the last index of the string 'Coding For All'
print(len(company) - 1)  # Output: 14

# Task 17: What character is at index 10 in the string 'Coding For All'
print(company[10])  # Output: A

# Task 18: Create an acronym for 'Python For Everyone'
acronym = "".join([word[0] for word in "Python For Everyone".split()])
print(acronym)  # Output: PFE

# Task 19: Create an acronym for 'Coding For All'
acronym2 = "".join([word[0] for word in "Coding For All".split()])
print(acronym2)  # Output: CFA

# Task 20: Use index to determine the position of the first occurrence of 'C' in 'Coding For All'
print(company.index('C'))  # Output: 0

# Task 21: Use index to determine the position of the first occurrence of 'F' in 'Coding For All'
print(company.index('F'))  # Output: 7

# Task 22: Use rfind to determine the position of the last occurrence of 'l' in 'Coding For All People'
print(company.rfind('l'))  # Output: 14

# Task 23: Use index or find to find the position of the first occurrence of the word 'because' in the sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  # Output: 32

# Task 24: Use rindex to find the position of the last occurrence of the word 'because'
print(sentence.rindex('because'))  # Output: 57

# Task 25: Slice out the phrase 'because because because' in the sentence
print(sentence[32:57])  # Output: because because because

# Task 26: Does 'Coding For All' start with a substring 'Coding'?
print(company.startswith('Coding'))  # Output: True

# Task 27: Does 'Coding For All' end with a substring 'coding'?
print(company.endswith('coding'))  # Output: False

# Task 28: Remove the left and right trailing spaces in the given string
company_with_spaces = '   Coding For All      '
print(company_with_spaces.strip())  # Output: Coding For All

# Task 29: Which one of the following variables return True when we use the method isidentifier()?
var1 = "30DaysOfPython"  # False (starts with a number)
var2 = "thirty_days_of_python"  # True
print(var1.isidentifier())  # Output: False
print(var2.isidentifier())  # Output: True

# Task 30: Join the list of Python libraries with a hash with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))  # Output: Django # Flask # Bottle # Pyramid # Falcon

# Task 31: Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# Task 32: Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Task 33: Use string formatting to display the area of a circle with radius 10
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Task 34: Make the following calculations using string formatting methods
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
