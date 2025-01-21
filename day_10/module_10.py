from functools import reduce

# Level 1 Exercises

# 1. Explain the difference between map, filter, and reduce:
# - map: Transforms each item in an iterable and returns a new iterable.
# - filter: Filters elements based on a condition.
# - reduce: Applies a function cumulatively to reduce an iterable to a single value.

# 2. Explain the difference between higher-order function, closure, and decorator:
# - Higher-order function: A function that takes a function as an argument or returns a function.
# - Closure: A function that retains access to variables from its lexical scope.
# - Decorator: A function that modifies the behavior of another function.

# 3. Define a call function before map, filter, or reduce
def multiply_by_two(x):
    return x * 2

numbers = [1, 2, 3, 4]
result = list(map(multiply_by_two, numbers))  # [2, 4, 6, 8]
print(result)

# 4. Use for loop to print each country in the countries list
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]
for country in countries:
    print(country)

# 5. Use for to print each name in the names list
names = ["John", "Alice", "Bob", "Diana"]
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# Level 2 Exercises

# 1. Use map to create a new list by changing each country to uppercase in the countries list
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]
upper_countries = list(map(lambda x: x.upper(), countries))  # ['FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']
print(upper_countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16]
print(squares)

# 3. Use map to change each name to uppercase in the names list
names = ["john", "alice", "bob"]
upper_names = list(map(lambda x: x.upper(), names))  # ['JOHN', 'ALICE', 'BOB']
print(upper_names)

# 4. Use filter to filter out countries containing 'land'
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]
land_countries = list(filter(lambda x: 'land' in x.lower(), countries))  # ['Finland', 'Iceland']
print(land_countries)

# 5. Use filter to filter out countries having exactly six characters
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]
six_char_countries = list(filter(lambda x: len(x) == 6, countries))  # ['Sweden']
print(six_char_countries)

# 6. Use filter to filter out countries containing six letters and more
long_countries = list(filter(lambda x: len(x) >= 6, countries))  # ['Finland', 'Sweden', 'Denmark', 'Iceland']
print(long_countries)

# 7. Use filter to filter out countries starting with an 'E'
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland", "Estonia"]
e_countries = list(filter(lambda x: x.startswith('E'), countries))  # ['Estonia']
print(e_countries)

# 8. Chain two or more list iterators (map, filter, reduce)
result = reduce(lambda x, y: x + ', ' + y, 
                list(map(lambda x: x.upper(), filter(lambda x: 'land' in x.lower(), countries))))
print(result)  # FINLAND, ICELAND

# 9. Declare a function called get_string_lists which takes a list as a parameter and returns a list containing only string items
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

mixed_list = [1, "apple", 3.14, "banana", True]
strings_only = get_string_lists(mixed_list)  # ['apple', 'banana']
print(strings_only)

# 10. Use reduce to sum all the numbers in the numbers list
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)  # 10
print(total)

# 11. Use reduce to concatenate all the countries and produce this sentence
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
sentence = reduce(lambda x, y: x + ", " + y, countries) + " are north European countries"
print(sentence)  # Estonia, Finland, Sweden, Denmark, Norway, Iceland are north European countries

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern
def categorize_countries(countries):
    patterns = ['land', 'ia', 'island', 'stan']
    categorized = [country for country in countries if any(pattern in country.lower() for pattern in patterns)]
    return categorized

countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland", "Estonia", "Kazakhstan"]
result = categorize_countries(countries)  # ['Finland', 'Iceland', 'Estonia', 'Kazakhstan']
print(result)

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter
def country_starting_letters(countries):
    letter_count = {}
    for country in countries:
        first_letter = country[0].upper()
        letter_count[first_letter] = letter_count.get(first_letter, 0) + 1
    return letter_count

countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland", "Estonia"]
result = country_starting_letters(countries)
print(result)  # {'F': 1, 'S': 1, 'D': 1, 'N': 1, 'I': 1, 'E': 1}

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries list
def get_first_ten_countries(countries):
    return countries[:10]

countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland", "Estonia", "Kazakhstan", "Russia", "USA", "India", "China"]
first_ten = get_first_ten_countries(countries)
print(first_ten)  # ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Estonia', 'Kazakhstan', 'Russia', 'USA', 'India']

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list
def get_last_ten_countries(countries):
    return countries[-10:]

countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland", "Estonia", "Kazakhstan", "Russia", "USA", "India", "China"]
last_ten = get_last_ten_countries(countries)
print(last_ten)  # ['Denmark', 'Norway', 'Iceland', 'Estonia', 'Kazakhstan', 'Russia', 'USA', 'India', 'China']
