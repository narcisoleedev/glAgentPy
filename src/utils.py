import json
import os

def saveToFile(data, filename): #Save data to a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f)

def loadFromFile(filename): #Load data from a JSON file
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None
