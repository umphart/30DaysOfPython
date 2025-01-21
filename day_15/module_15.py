import requests
from collections import Counter
import numpy as np
import statistics
from bs4 import BeautifulSoup

# Exercise 1: Finding the 10 Most Frequent Words in "Romeo and Juliet"
def find_most_frequent_words_in_romeo_and_juliet():
    # URL of the text file
    romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
    
    # Fetch the content of the URL
    response = requests.get(romeo_and_juliet)
    text = response.text
    
    # Clean and tokenize the text
    words = re.findall(r'\w+', text.lower())  # \w+ matches all words (alphanumeric)
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the 10 most frequent words
    most_common_words = word_counts.most_common(10)
    
    return most_common_words

# Exercise 2: Cats API - Min, Max, Mean, Median, Standard Deviation of Weight and Lifespan
def cats_api_stats():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    
    # Fetch the data
    response = requests.get(cats_api)
    cats_data = response.json()
    
    # Extract the weights and lifespans
    weights = [cat['weight']['metric'] for cat in cats_data if 'weight' in cat]
    lifespans = [cat['life_span'] for cat in cats_data if 'life_span' in cat]
    
    # Convert weight to float
    weights = [float(weight.split()[0]) for weight in weights]
    
    # Calculate min, max, mean, median, and standard deviation
    weight_min = min(weights)
    weight_max = max(weights)
    weight_mean = np.mean(weights)
    weight_median = np.median(weights)
    weight_stddev = np.std(weights)
    
    lifespan_min = min(lifespans)
    lifespan_max = max(lifespans)
    lifespan_mean = np.mean(lifespans)
    lifespan_median = np.median(lifespans)
    lifespan_stddev = np.std(lifespans)
    
    return {
        'Weight Stats': {
            'Min': weight_min,
            'Max': weight_max,
            'Mean': weight_mean,
            'Median': weight_median,
            'Standard Deviation': weight_stddev
        },
        'Lifespan Stats': {
            'Min': lifespan_min,
            'Max': lifespan_max,
            'Mean': lifespan_mean,
            'Median': lifespan_median,
            'Standard Deviation': lifespan_stddev
        }
    }

# Exercise 3: Create Frequency Table of Country and Breed of Cats
def create_cat_frequency_table():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    
    # Fetch the data
    response = requests.get(cats_api)
    cats_data = response.json()
    
    # Get breed and country
    countries_and_breeds = [(cat['origin'], cat['name']) for cat in cats_data if 'origin' in cat and 'name' in cat]
    
    # Create frequency table
    frequency_table = Counter(countries_and_breeds)
    
    return frequency_table

# Exercise 4: Countries API - 10 Largest Countries, 10 Most Spoken Languages, Total Languages
def countries_api_stats():
    countries_api = 'https://restcountries.com/v3.1/all'
    
    # Fetch the data
    response = requests.get(countries_api)
    countries_data = response.json()
    
    # Find the 10 largest countries by population
    largest_countries = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)[:10]
    
    # Find the 10 most spoken languages
    languages = {}
    for country in countries_data:
        for language in country.get('languages', {}).values():
            languages[language] = languages.get(language, 0) + 1
    
    # Sort and get the 10 most spoken languages
    most_spoken_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Find the total number of languages
    total_languages = len(languages)
    
    return {
        'Largest Countries': [(country['name']['common'], country['population']) for country in largest_countries],
        'Most Spoken Languages': most_spoken_languages,
        'Total Languages': total_languages
    }

# Exercise 5: Scrape UCI Dataset Page using BeautifulSoup
def scrape_uci_datasets():
    uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
    
    # Fetch the page content
    response = requests.get(uci_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the dataset names and their descriptions
    datasets = soup.find_all('td', {'class': 'name'})
    
    # Print the first 5 dataset names
    datasets_names = [dataset.get_text() for dataset in datasets[:5]]
    
    return datasets_names

# Main execution (testing each function)
if __name__ == '__main__':
    # Test Exercise 1: Most Frequent Words in Romeo and Juliet
    print("Most Frequent Words in Romeo and Juliet:")
    print(find_most_frequent_words_in_romeo_and_juliet())

    # Test Exercise 2: Cats API Stats (Weight and Lifespan)
    print("\nCats API Stats (Weight and Lifespan):")
    print(cats_api_stats())

    # Test Exercise 3: Frequency Table of Country and Breed of Cats
    print("\nFrequency Table of Country and Breed of Cats:")
    print(create_cat_frequency_table())

    # Test Exercise 4: Countries API Stats (Largest Countries, Most Spoken Languages)
    print("\nCountries API Stats:")
    print(countries_api_stats())

    # Test Exercise 5: Scrape UCI Datasets
    print("\nUCI Datasets (Top 5):")
    print(scrape_uci_datasets())
