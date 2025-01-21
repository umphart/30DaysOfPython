# API and HTTP Example File

import requests
import json

# Part 1: Understanding APIs and HTTP

"""
An API (Application Programming Interface) is a set of rules that allow software applications to communicate with each other.
APIs are used to expose data or functionalities to other applications, and they rely on HTTP for communication over the web.

HTTP (HyperText Transfer Protocol) is the protocol used for transferring data over the web. It defines how requests and responses are structured.

Common HTTP Methods:
- GET: Retrieves data from the server.
- POST: Sends data to the server.
- PUT: Updates an existing resource.
- DELETE: Deletes a specified resource.
- PATCH: Partially updates a resource.

Common HTTP Status Codes:
- 200 OK: Request was successful.
- 201 Created: A resource was successfully created.
- 400 Bad Request: Request was malformed.
- 401 Unauthorized: Authentication is required.
- 404 Not Found: The requested resource could not be found.
- 500 Internal Server Error: Server encountered an error.
"""

# Part 2: Interacting with an API using Python (The Cat API Example)

def get_cat_breeds():
    """
    This function interacts with the Cat API and retrieves a list of cat breeds.
    The response is processed and the name of the first breed is printed.
    """
    url = 'https://api.thecatapi.com/v1/breeds'

    # Sending GET request to the API
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        cat_breeds = response.json()
        
        # Printing the name of the first cat breed
        print(f"The first cat breed is: {cat_breeds[0]['name']}")
    else:
        # Handling failure
        print(f"Failed to retrieve data: {response.status_code}")

# Part 3: Sending POST request to an API

def create_new_user():
    """
    This function demonstrates how to send a POST request with JSON data to create a new user.
    """
    url = 'https://example.com/api/users'  # Placeholder URL for demonstration
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    # Sending POST request with JSON data
    response = requests.post(url, json=data)

    # Checking if the user was created successfully (HTTP status code 201)
    if response.status_code == 201:
        print("User created successfully!")
    else:
        print(f"Failed to create user: {response.status_code}")

# Part 4: Example of accessing a resource (Romeo and Juliet text)

def get_romeo_and_juliet_text():
    """
    This function retrieves the text of Romeo and Juliet from Project Gutenberg and prints a part of it.
    """
    romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'

    # Sending GET request to retrieve the text
    response = requests.get(romeo_and_juliet_url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Printing the first 500 characters of the text as an example
        print(response.text[:500])  # Displaying first 500 characters of the text
    else:
        print(f"Failed to retrieve the text: {response.status_code}")

# Part 5: Handling HTTP Requests and Response

def check_http_status():
    """
    This function demonstrates how to check the HTTP response status and handle different status codes.
    """
    url = 'https://httpbin.org/status/404'  # This will return a 404 error

    # Sending GET request
    response = requests.get(url)

    # Checking the status code
    if response.status_code == 200:
        print("Request was successful!")
    elif response.status_code == 404:
        print("Error: Resource not found (404)")
    else:
        print(f"Error: Received status code {response.status_code}")

# Example function calls

if __name__ == '__main__':
    print("Getting Cat Breeds...")
    get_cat_breeds()

    print("\nCreating New User...")
    create_new_user()

    print("\nFetching Romeo and Juliet Text...")
    get_romeo_and_juliet_text()

    print("\nChecking HTTP Status...")
    check_http_status()
