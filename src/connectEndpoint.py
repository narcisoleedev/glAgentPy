import requests

def connectEndpoint(base, endpoint): #JUST GET FOR NOW
    url = f"http://{base}/{endpoint}" #Things endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  #Returns the things
    return []