# Loops Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# Using for loop (reverse order)
for i in range(10, -1, -1):
    print(i)

# Using while loop (reverse order)
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# #
# ##
# ###
# ####
# #####
# ######
# #######

for i in range(1, 8):
    print("#" * i)

# 4. Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for i in range(8):
    print("# " * 8)

# 5. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lang in languages:
    print(lang)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print(i)


# Loops Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers from 0 to 100 is {total_sum}")

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")


# Loops Exercises: Level 3

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# Assuming you have a list of countries
countries = ['Finland', 'Iceland', 'Ireland', 'Germany', 'Netherlands', 'Sweden', 'Denmark']
countries_with_land = []

for country in countries:
    if "land" in country:
        countries_with_land.append(country)

print("Countries containing 'land':", countries_with_land)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print("Reversed fruit list:", reversed_fruits)


# 3. Go to the data folder and use the countries_data.py file.
# Let's assume the countries_data.py contains a list of countries with languages and population data.
# Example of how this could work:

countries_data = [
    {"country": "USA", "languages": ["English", "Spanish"], "population": 331},
    {"country": "China", "languages": ["Mandarin"], "population": 1441},
    {"country": "India", "languages": ["Hindi", "English"], "population": 1380},
    {"country": "Russia", "languages": ["Russian"], "population": 146},
    {"country": "Brazil", "languages": ["Portuguese"], "population": 213}
]

# 3.1. What are the total number of languages in the data?
total_languages = set()
for country in countries_data:
    total_languages.update(country["languages"])

print("Total number of unique languages:", len(total_languages))

# 3.2. Find the ten most spoken languages from the data
# For simplicity, we'll count the number of occurrences of each language
language_count = {}
for country in countries_data:
    for language in country["languages"]:
        language_count[language] = language_count.get(language, 0) + 1

# Sorting by count (most spoken languages first)
most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
print("Top spoken languages:", most_spoken_languages[:10])

# 3.3. Find the 10 most populated countries in the world
sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
print("Top 10 most populated countries:", sorted_countries[:10])
