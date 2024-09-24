import requests

def fetchThings(wotDirectory):
    url = f"http://{wotDirectory["ip"]}:{wotDirectory["port"]}/things" #Things endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns the things
    return []
