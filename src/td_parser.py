def list_endpoints(thing):
    endpoints = []
    if 'base' in thing and 'actions' in thing:
        base_url = thing['base']
        for action_name, action_info in thing['actions'].items():
            endpoint = f"{base_url}/{action_info['href']}"
            endpoints.append(endpoint)
    return endpoints
