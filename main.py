import argparse
import json
from src.discovery import discoverWotDir
from src.wotDirectory import fetchThings
from src.tdParser import listEndpoints
import src.utils as utils

jsonSave = 'wotDirectories.json'
thingsSave = 'things.json'

def discover():

    wotDirectories = discoverWotDir()

    if wotDirectories:
        for i, directory in enumerate(wotDirectories):
            print(f"[{i}] {directory}")
        
        utils.saveToFile([str(directory) for directory in wotDirectories], jsonSave)

    else:
        print("No WoT directories found")

def connect(index):
    
    wotDirectories = utils.loadFromFile(jsonSave) 
    jsonString = wotDirectories[index].replace("'", '"') #String treatment
    jsonString = jsonString.replace('b"', '"').replace('None', 'null')
    wotDirectory = json.loads(jsonString) #Transform to dict
    
    if 0 <= index < len(wotDirectories): #If there is the said index
 
        ip =  wotDirectory['ip']
        port = wotDirectory['port']
        print(f"Connecting to WoT Directory at: {ip}...")
        portNIp = {
            "ip": ip,
            "port": port
        }
        things = fetchThings(portNIp)  #Fetch things from the directory

        if things: #If it returns things
            for i, thing in enumerate(things):
                print(f"[{i}] {thing['id']}")

            utils.saveToFile(things, "things.json")
            
        else:
            print(f"No things found in directory: {directory_ip}")
    else:
        print("Invalid directory index!")

def listThings():
    things = utils.loadFromFile(thingsSave)
    if things:
        for i, thing in enumerate(things):
            print(f"Device {i + 1}:")
            print(f"  Title: {thing.get('title')}")
            print(f"  ID: {thing.get('id')}")
            print(f"  Base URL: {thing.get('base', 'Not available')}")
            
            if 'actions' in thing: #If there are "actions" property
                print("  Actions:")
                for action, details in thing['actions'].items():
                    print(f"    {action}: {details.get('forms', [{}])[0].get('href')}")

            if 'properties' in thing: #If there are "properties" property
                print("  Properties:")
                for prop, details in thing['properties'].items():
                    print(f"    {prop}: {details.get('forms', [{}])[0].get('href')}")

            print("-" * 40)
    else:
        print("No things connected. Use 'gl connect' to connect to a directory.")

def listThingsEndpoint(index):
    things = utils.loadFromFile(thingsSave)
    if 0 <= index < len(things):
        thing = things[index]
        endpoints = listEndpoints(thing)
        if endpoints:
            print(f"Endpoints for Thing '{thing["id"]}':")
            for endpoint in endpoints:
                print(endpoint)
        else:
            print("No endpoints found for this Thing")
    else:
        print("Invalid thing index!")

def main():
    global wotDirectories, things
 
    wotDirectories = utils.loadFromFile(jsonSave) or [] #Load previously saved directories and things
    things = utils.loadFromFile(thingsSave) or []

    parser = argparse.ArgumentParser(description="GLAgent CLI for WoT")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser('discover', help="Discover WoT directories") #Discover WoT directories

    connect_parser = subparsers.add_parser('connect', help="Connect to a WoT directory")  #Connect to WoT directory
    connect_parser.add_argument('index', type=int, help="Index of the directory to connect to")

    subparsers.add_parser('list', help="List all Things in the connected WoT directory") #List all things

    endpoint_parser = subparsers.add_parser('endpoints', help="List all endpoints of a specific Thing") #List all endpoints for a specific thing
    endpoint_parser.add_argument('index', type=int, help="Index of the Thing to list endpoints for")

    args = parser.parse_args()

    if args.command == 'discover':
        discover()

    elif args.command == 'connect':
        connect(args.index)

    elif args.command == 'list':
        listThings()

    elif args.command == 'endpoints':
        listThingsEndpoint(args.index)

if __name__ == "__main__":
    main()
