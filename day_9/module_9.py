# List Comprehensions Exercises

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("Negative and zero:", negative_and_zero)
# Output: Negative and zero: [-4, -3, -2, -1, 0]

# 2. Flatten the list of lists of lists to a one-dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print("Flattened list:", flattened_list)
# Output: Flattened list: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Create the list of tuples using list comprehension
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples:", tuple_list)
# Output: List of tuples:
# [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32), ...]

# 4. Flatten the countries list and convert to desired format
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print("Flattened countries:", flattened_countries)
# Output: Flattened countries: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Change the countries list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dicts = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print("Countries as dictionaries:", country_dicts)
# Output: Countries as dictionaries:
# [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

# 6. Change the list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{name[0][0]} {name[0][1]}" for name in names]
print("Concatenated names:", concatenated_names)
# Output: Concatenated names: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# Lambda function to calculate slope or y-intercept of linear functions
# The linear equation is: y = mx + b
# Where m is the slope, and b is the y-intercept.

# Lambda function to calculate the slope (m) given two points (x1, y1) and (x2, y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate the y-intercept (b) given the slope (m) and a point (x1, y1)
y_intercept = lambda m, x1, y1: y1 - m * x1

# Example for slope
m = slope(1, 2, 3, 4)  # Slope between points (1,2) and (3,4)
print("Slope (m):", m)
# Output: Slope (m): 1.0

# Example for y-intercept
b = y_intercept(m, 1, 2)  # Using slope m, and point (1, 2)
print("Y-intercept (b):", b)
# Output: Y-intercept (b): 1.0
