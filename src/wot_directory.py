import requests

def fetch_tds(wot_directory_ip):
    url = f"http://{wot_directory_ip}/td"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def fetch_things(wot_directory_ip):
    url = f"http://{wot_directory_ip}/things"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the response is a JSON list of Things
    return []
