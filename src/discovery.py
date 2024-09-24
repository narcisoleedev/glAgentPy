import time
import socket
from zeroconf import Zeroconf, ServiceBrowser, ServiceListener

class MyListener(ServiceListener):
    def __init__(self):
        self.wot_directories = []

    def add_service(self, zeroconf, service_type, name):
        info = zeroconf.get_service_info(service_type, name)
        if info:
            ip = socket.inet_ntoa(info.addresses[0]) # Converte de 32bit para decimal
            info_data = {
                "name": name,
                "ip": ip,
                "port": info.port,
                "properties": info.properties
            }
            self.wot_directories.append(info_data)

def discoverWotDir():
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_wot._tcp.local.", listener)

    # Allow some time for discovery
    time.sleep(5)

    # Print directories with readable IP addresses
    for directory in listener.wot_directories:
        print(f"Service: {directory['name']}, IP: {directory['ip']}, Port: {directory['port']}, Properties: {directory['properties']}")
    
    zeroconf.close()

    return listener.wot_directories
