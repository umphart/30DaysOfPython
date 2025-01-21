# Day 5: 30 Days of Python Programming - Sets Exercises

# Level 1

# 1. Find the length of the set it_companies
it_companies = {"Google", "Facebook", "Microsoft", "Apple", "IBM", "Oracle"}
print(len(it_companies))  # Output: 6

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)  # Output: {'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Twitter'}

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Amazon", "Tesla", "Netflix"])
print(it_companies)  # Output: {'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Twitter', 'Amazon', 'Tesla', 'Netflix'}

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Tesla")
print(it_companies)  # Output: {'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Twitter', 'Amazon', 'Netflix'}

# 5. What is the difference between remove and discard
# remove() raises an error if the element doesn't exist in the set
# discard() does not raise an error if the element doesn't exist in the set

# Trying to remove a non-existing company (this will raise an error)
# it_companies.remove("Spotify")  # Will raise a KeyError

# Trying to discard a non-existing company (this will not raise an error)
it_companies.discard("Spotify")  # No error

# Level 2

# 1. Join A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A.union(B)  # A | B: {1, 2, 3, 4, 5, 6, 7, 8}

# 2. Find A intersection B
intersection = A.intersection(B)
print(intersection)  # Output: {4, 5}

# 3. Is A a subset of B?
print(A.issubset(B))  # Output: False

# 4. Are A and B disjoint sets?
print(A.isdisjoint(B))  # Output: False (because they share common elements {4, 5})

# 5. Join A with B and B with A
# A | B or B | A would result in the same union
union_A_B = A.union(B)
union_B_A = B.union(A)
print(union_A_B)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(union_B_A)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 6. What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print(symmetric_diff)  # Output: {1, 2, 3, 6, 7, 8}

# 7. Delete the sets completely
del A
del B
# print(A)  # This will raise an error because A has been deleted
# print(B)  # This will raise an error because B has been deleted

# Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_list = [18, 20, 22, 22, 18, 25, 20, 30, 30, 25, 25]
ages_set = set(ages_list)

print(len(ages_list))  # Output: 11
print(len(ages_set))   # Output: 6

# List has duplicates, so it is larger than the set (which contains unique values)

# 2. Explain the difference between the following data types: string, list, tuple and set
# string: An immutable sequence of characters.
# list: An ordered, mutable collection of items (can contain duplicates).
# tuple: An ordered, immutable collection of items (can contain duplicates).
# set: An unordered, mutable collection of unique items (no duplicates allowed).

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()  # Split sentence into words
unique_words = set(words)  # Convert list of words into a set to get unique words
print(len(unique_words))  # Output: 8 (unique words)

