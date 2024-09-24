import time
import socket
from zeroconf import Zeroconf, ServiceBrowser, ServiceListener

class MyListener(ServiceListener):
    def __init__(self):
        self.wotDirectories = []

    def add_service(self, zeroconf, serviceType, name):
        info = zeroconf.get_service_info(serviceType, name)
        if info:
            ip = socket.inet_ntoa(info.addresses[0]) #32bit to decimal
            infoData = {
                "name": name,
                "ip": ip,
                "port": info.port,
                "properties": info.properties
            }
            self.wotDirectories.append(infoData)

def discoverWotDir():
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_wot._tcp.local.", listener)

    time.sleep(5) #Allow some time for discovery

    for directory in listener.wotDirectories: #Print directories with readable IP addresses
        print(f"Service: {directory['name']}, IP: {directory['ip']}, Port: {directory['port']}, Properties: {directory['properties']}")
    
    zeroconf.close() #Close connection

    return listener.wotDirectories
