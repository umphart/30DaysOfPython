import os
import json
import re
from collections import Counter

# Level 1: Count the number of lines and words in the files

def count_lines_and_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

def count_speech_lines_and_words():
    filenames = [
        './data/obama_speech.txt',
        './data/michelle_obama_speech.txt',
        './data/donald_speech.txt',
        './data/melina_trump_speech.txt'
    ]
    
    for filename in filenames:
        num_lines, num_words = count_lines_and_words(filename)
        print(f"File: {filename} - Lines: {num_lines}, Words: {num_words}")

# Level 1: Read countries_data.json and find most spoken languages

def most_spoken_languages(filename, top_n):
    with open(filename, 'r') as f:
        data = json.load(f)
        
    languages = []
    for country in data['countries']:
        for language in country['languages']:
            languages.append(language)
    
    language_counts = Counter(languages)
    return language_counts.most_common(top_n)

# Level 1: Read countries_data.json and find most populated countries

def most_populated_countries(filename, top_n):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    countries = [{'country': country['country'], 'population': country['population']} for country in data['countries']]
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

# Level 2: Extract incoming email addresses from email_exchange_big.txt

def extract_email_addresses(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)

# Level 2: Find most common words in a text or file

def find_most_common_words(text, n):
    if os.path.exists(text):  # If the input is a file
        with open(text, 'r') as file:
            text = file.read()
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase
    word_counts = Counter(words)
    return word_counts.most_common(n)

# Level 2: Find most frequent words in Obama, Michelle, Trump, and Melina's speeches

def most_frequent_words_speech():
    filenames = [
        './data/obama_speech.txt',
        './data/michelle_obama_speech.txt',
        './data/donald_speech.txt',
        './data/melina_trump_speech.txt'
    ]
    
    for filename in filenames:
        print(f"Most frequent words in {filename}:")
        most_common = find_most_common_words(filename, 10)
        print(most_common)

# Level 2: Check similarity between two texts

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

def remove_support_words(text, stop_words):
    words = text.split()
    return [word for word in words if word not in stop_words]

def check_text_similarity(text1, text2, stop_words_file='./data/stopwords.txt'):
    with open(stop_words_file, 'r') as file:
        stop_words = set(file.read().splitlines())
    
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    
    cleaned_text1 = remove_support_words(cleaned_text1, stop_words)
    cleaned_text2 = remove_support_words(cleaned_text2, stop_words)
    
    common_words = set(cleaned_text1).intersection(set(cleaned_text2))
    similarity_percentage = len(common_words) / len(set(cleaned_text1).union(set(cleaned_text2))) * 100
    return similarity_percentage

# Level 2: Find 10 most repeated words in romeo_and_juliet.txt

def most_repeated_words_in_romeo_and_juliet():
    with open('./data/romeo_and_juliet.txt', 'r') as file:
        text = file.read()
    common_words = find_most_common_words(text, 10)
    print(common_words)

# Level 2: Count occurrences of Python, JavaScript, Java in Hacker News CSV

def count_keywords_in_hacker_news_csv(filename):
    python_count = 0
    js_count = 0
    java_count = 0
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'python' in line.lower():
                python_count += 1
            if 'javascript' in line.lower():
                js_count += 1
            if 'java' in line.lower() and 'javascript' not in line.lower():
                java_count += 1
    
    print(f"Python mentions: {python_count}")
    print(f"JavaScript mentions: {js_count}")
    print(f"Java mentions (excluding JavaScript): {java_count}")

# Calling the functions to demonstrate functionality
if __name__ == "__main__":
    # Level 1: Count lines and words
    count_speech_lines_and_words()

    # Level 1: Most spoken languages
    print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))
    print(most_spoken_languages(filename='./data/countries_data.json', top_n=3))

    # Level 1: Most populated countries
    print(most_populated_countries(filename='./data/countries_data.json', top_n=10))
    print(most_populated_countries(filename='./data/countries_data.json', top_n=3))

    # Level 2: Extract email addresses
    email_addresses = extract_email_addresses('./data/email_exchange_big.txt')
    print(email_addresses)

    # Level 2: Most common words in a file
    print(find_most_common_words('./data/sample.txt', 10))

    # Level 2: Most frequent words in speeches
    most_frequent_words_speech()

    # Level 2: Check similarity between two speeches
    with open('./data/michelle_obama_speech.txt', 'r') as file:
        michelle_text = file.read()
    with open('./data/melina_trump_speech.txt', 'r') as file:
        melina_text = file.read()
    
    similarity = check_text_similarity(michelle_text, melina_text)
    print(f"Text similarity between Michelle's and Melina's speech: {similarity}%")

    # Level 2: Most repeated words in Romeo and Juliet
    most_repeated_words_in_romeo_and_juliet()

    # Level 2: Count mentions in Hacker News CSV
    count_keywords_in_hacker_news_csv('./data/hacker_news.csv')
