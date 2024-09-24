import requests

def fetch_tds(wot_directory_ip):
    url = f"http://{wotDirectory["ip"]}:{wotDirectory["port"]}/td"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def fetch_things(wotDirectory):
    url = f"http://{wotDirectory["ip"]}:{wotDirectory["port"]}/things"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the response is a JSON list of Things
    return []
