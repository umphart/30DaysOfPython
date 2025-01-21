import re
from collections import Counter

# Level 1: Most Frequent Word in the Paragraph
def most_frequent_word(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())  # \b\w+\b matches word boundaries and alphanumeric characters
    word_counts = Counter(words)
    most_frequent = word_counts.most_common(1)
    return most_frequent[0][0], most_frequent[0][1]

# Find the distance between the two furthest particles
def distance_between_furthest_particles(text):
    points = list(map(int, re.findall(r'-?\d+', text)))  # -?\d+ will match both positive and negative numbers
    sorted_points = sorted(points)
    distance = sorted_points[-1] - sorted_points[0]
    return distance

# Level 2: Valid Python Variable
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_]\w*$'
    return bool(re.match(pattern, variable))

# Level 3: Clean Text and Find Most Frequent Words
def clean_text(sentence):
    cleaned_text = re.sub(r'[^\w\s]', '', sentence)  # Remove unwanted characters and normalize the text
    cleaned_text = cleaned_text.lower()  # Convert to lowercase
    return cleaned_text

def most_frequent_words(cleaned_text):
    words = cleaned_text.split()
    word_counts = Counter(words)
    return word_counts.most_common(3)

# Test Data for Level 1
paragraph = """I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to 
develop an application what else can you love."""

# Most Frequent Word Exercise
word, count = most_frequent_word(paragraph)
print(f"Most frequent word: {word} with {count} occurrences.")

# Test Data for Distance Between Particles
text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction.'''
distance = distance_between_furthest_particles(text)
print(f"The distance between the two furthest particles is: {distance}")

# Test Data for Level 2
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True

# Test Data for Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
print(most_frequent_words(cleaned_text))  # [(3, 'i'), (2, 'teaching'), (2, 'and')]
