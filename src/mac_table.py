import napalm
from tabulate import tabulate
 
def main():
 
    driver_ios = napalm.get_network_driver("ios")
 
    device_list = [["192.168.155.2","ios", "core-switch"],["192.168.155.50", "ios", "router"]]
 
    network_devices = []
    network_devices.append(
                            driver_ios(
                            hostname = device[0],
                            username = "ciscoadmin",
                            password = "!qAz@wSx#eDc"
                           )
 
    devices_table = [["hostname", "vendor", "model", "uptime", "serial_number"]]
    devices_table_int = [["hostname","interface","is_up", "is_enabled", "description", "speed", "mtu", "mac_address"]]
    devices_mac_table = [["hostname","mac", "interface", "vlan", "static"]]
     
    for device in network_devices:
        print("Connecting to {} ...".format(device.hostname))
        device.open()
 
        print("Getting device facts")
        device_facts = device.get_facts()
 
        devices_table.append([device_facts["hostname"],
                              device_facts["vendor"],
                              device_facts["model"],
                              device_facts["uptime"],
                              device_facts["serial_number"]
                              ])
 
        print("Getting device interfaces")
        device_interfaces = device.get_interfaces()
        for interface in device_interfaces:
            if device_interfaces[interface]['is_up']:    
                devices_table_int.append([device_facts["hostname"],
                                      interface,
                                      device_interfaces[interface]['is_up'],
                                      device_interfaces[interface]['is_enabled'],
                                      device_interfaces[interface]['description'],
                                      device_interfaces[interface]['speed'],
                                      device_interfaces[interface]['mtu'],
                                      device_interfaces[interface]['mac_address']
 
        ])
     
        if "SW" in device_facts["hostname"]:
            print("Getting Mac Address Table from Switch")
            device_mac_info = device.get_mac_address_table()
            for mac_entry in device_mac_info:
                devices_mac_table.append([device_facts["hostname"],
                                          mac_entry["mac"],
                                          mac_entry["interface"],
                                          mac_entry["vlan"],
                                          mac_entry["static"],                
                ])
 
        device.close()
        print("Done.")
    print(tabulate(devices_table, headers="firstrow"))
    print()
    print(tabulate(devices_table_int, headers="firstrow"))
    print()
    print(tabulate(devices_mac_table, headers="firstrow"))
    print()
 
if __name__ == '__main__':
    main()
