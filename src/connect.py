import requests

def connectThing(baseUrl, endpoint):
    url = f'{baseUrl}{endpoint}' 
    print(f"Connecting to URL: {url}")
    
    try:
        response = requests.get(url)
        print(f"Response content: {response.content}")  
        if response.status_code == 200:
            if response.headers.get('Content-Type') == 'application/json':
                return response.json()  # Return parsed JSON
            else:
                return response.text  # Return the rawwwwrrr text
        else:
            print(f"Unexpected status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")  
    
    return []