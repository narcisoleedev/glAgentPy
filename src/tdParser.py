def listEndpoints(thing):
    endpoints = []
    if 'base' in thing and 'actions' in thing:
        base_url = thing['base']
        for actionName, actionInfo in thing['actions'].items():
            if(actionInfo['href']):
                endpoint = f"{base_url}/{actionInfo['href']}"
                endpoints.append(endpoint)
    return endpoints
