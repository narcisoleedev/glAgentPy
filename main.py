import argparse
from src.discovery import discover_wot_directories
from src.wot_directory import fetch_tds, fetch_things
from src.td_parser import list_endpoints
import src.utils as utils

# Store WoT directories and things globally
wot_directories = []
things = []

def discover():
    global wot_directories
    wot_directories = discover_wot_directories()

    if wot_directories:
        for i, directory in enumerate(wot_directories):
            print(f"[{i}] {directory}")
        # Save directories to a JSON file
        utils.save_to_file([str(directory) for directory in wot_directories], "wot_directories.json")
    else:
        print("No WoT directories found")

def connect(directory_index):
    global things
    if 0 <= directory_index < len(wot_directories):
        directory_ip = wot_directories[directory_index].server  # Assuming .server contains IP
        print(f"Connecting to WoT Directory at {directory_ip}...")
        things = fetch_things(directory_ip)  # Fetch Things from the directory

        if things:
            for i, thing in enumerate(things):
                print(f"[{i}] {thing['id']}")
            # Save things to a JSON file
            utils.save_to_file(things, "things.json")
        else:
            print(f"No things found in directory {directory_ip}")
    else:
        print("Invalid directory index!")

def list_things():
    if things:
        for i, thing in enumerate(things):
            print(f"[{i}] {thing['id']}")
    else:
        print("No things connected. Use 'gl connect' to connect to a directory.")

def list_thing_endpoints(thing_index):
    if 0 <= thing_index < len(things):
        thing = things[thing_index]
        endpoints = list_endpoints(thing)
        if endpoints:
            print(f"Endpoints for Thing '{thing['id']}':")
            for endpoint in endpoints:
                print(endpoint)
        else:
            print("No endpoints found for this Thing")
    else:
        print("Invalid thing index!")

def main():
    global wot_directories, things

    # Load previously saved directories and things
    wot_directories = utils.load_from_file("wot_directories.json") or []
    things = utils.load_from_file("things.json") or []

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
