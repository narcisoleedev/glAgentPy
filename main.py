import argparse
import json
from src.discovery import discoverWotDir
from src.wot_directory import fetch_tds, fetch_things
from src.td_parser import list_endpoints
import src.utils as utils

jsonSave = 'wotDirectories.json'
thingsSave = 'things.json'

def discover():

    wotDirectories = discoverWotDir()

    if wotDirectories:
        for i, directory in enumerate(wotDirectories):
            print(f"[{i}] {directory}")
        # Save directories to a JSON file
        utils.save_to_file([str(directory) for directory in wotDirectories], jsonSave)
    else:
        print("No WoT directories found")

def connect(index):
    
    wotDirectories = utils.loadFromFile(jsonSave)
    jsonString = wotDirectories[index].replace("'", '"')
    jsonString = jsonString.replace('b"', '"').replace('None', 'null')
    wotDirectory = json.loads(jsonString)
    
    if 0 <= index < len(wotDirectories):

        ip =  wotDirectory['ip']
        port = wotDirectory['port']
        print(f"Connecting to WoT Directory at {ip}...")
        portNIp = {
            "ip": ip,
            "port": port
        }
        things = fetch_things(portNIp)  # Fetch Things from the directory

        if things:
            for i, thing in enumerate(things):
                print(f"[{i}] {thing['id']}")

            utils.save_to_file(things, "things.json")
            
        else:
            print(f"No things found in directory {directory_ip}")
    else:
        print("Invalid directory index!")

def list_things():
    things = utils.loadFromFile(thingsSave)
    if things:
        for i, thing in enumerate(things):
            print(f"Device {i + 1}:")
            print(f"  Title: {thing.get('title')}")
            print(f"  ID: {thing.get('id')}")
            print(f"  Base URL: {thing.get('base', 'Not available')}")
            
            # Print the actions if they exist
            if 'actions' in thing:
                print("  Actions:")
                for action, details in thing['actions'].items():
                    print(f"    {action}: {details.get('forms', [{}])[0].get('href')}")

            # Print the properties if they exist
            if 'properties' in thing:
                print("  Properties:")
                for prop, details in thing['properties'].items():
                    print(f"    {prop}: {details.get('forms', [{}])[0].get('href')}")

            print("-" * 40)
    else:
        print("No things connected. Use 'gl connect' to connect to a directory.")

def list_thing_endpoints(index):
    things = utils.loadFromFile(thingsSave)
    if 0 <= index < len(things):
        thing = things[index]
        endpoints = list_endpoints(thing)
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

    # Load previously saved directories and things
    wotDirectories = utils.loadFromFile(jsonSave) or []
    things = utils.loadFromFile("things.json") or []

    # Continue with argument parsing and function calls
    parser = argparse.ArgumentParser(description="GLAgent CLI for WoT")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Discover WoT directories
    subparsers.add_parser('discover', help="Discover WoT directories")

    # Connect to WoT directory
    connect_parser = subparsers.add_parser('connect', help="Connect to a WoT directory")
    connect_parser.add_argument('index', type=int, help="Index of the directory to connect to")

    # List all Things
    subparsers.add_parser('list', help="List all Things in the connected WoT directory")

    # List all endpoints for a specific Thing
    endpoint_parser = subparsers.add_parser('endpoints', help="List all endpoints of a specific Thing")
    endpoint_parser.add_argument('index', type=int, help="Index of the Thing to list endpoints for")

    args = parser.parse_args()

    if args.command == 'discover':
        discover()

    elif args.command == 'connect':
        connect(args.index)

    elif args.command == 'list':
        list_things()

    elif args.command == 'endpoints':
        list_thing_endpoints(args.index)

if __name__ == "__main__":
    main()
