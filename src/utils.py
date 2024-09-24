import json
import os

# Save data to a JSON file
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Load data from a JSON file
def loadFromFile(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None
