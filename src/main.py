#!/usr/bin/python
import napalm
from tabulate import tabulate


def main():
    driver_ios = napalm.get_network_driver('ios')

    device_list = [
        ['192.168.155.2', 'ios', 'switch'],
        ['192.168.155.3', 'ios', 'switch'],
        ['192.168.155.4', 'ios', 'switch'],
        ['192.168.155.7', 'ios', 'switch'],
        ['192.168.155.21', 'ios', 'switch'],
        ['192.168.155.22', 'ios', 'switch'],
        ['192.168.155.24', 'ios', 'switch'],
        ['192.168.155.25', 'ios', 'switch'],
        ['192.168.155.26', 'ios', 'switch'],
        ['192.168.155.27', 'ios', 'switch'],
        ['192.168.155.28', 'ios', 'switch'],
        ['192.168.155.29', 'ios', 'switch'],
        ['192.168.155.30', 'ios', 'switch'],
        ['192.168.155.31', 'ios', 'switch'],
        ['192.168.155.32', 'ios', 'switch'],
        ['192.168.155.33', 'ios', 'switch'],
        ['192.168.155.34', 'ios', 'switch'],
        ['192.168.155.35', 'ios', 'switch'],
        ['192.168.155.36', 'ios', 'switch'],
        ['192.168.155.37', 'ios', 'switch'],
        ['192.168.155.38', 'ios', 'switch'],
        ['192.168.155.39', 'ios', 'switch'],
        ['192.168.155.40', 'ios', 'switch'],
        ['192.168.155.41', 'ios', 'switch'],
        ['192.168.155.42', 'ios', 'switch'],
        ['192.168.155.43', 'ios', 'switch'],
        ['192.168.155.44', 'ios', 'switch'],
        ['192.168.155.45', 'ios', 'switch'],
        ['192.168.155.46', 'ios', 'switch'],
        ['192.168.155.47', 'ios', 'switch'],
        ['192.168.155.49', 'ios', 'switch'],
    ]

    network_devices = []
    for device in device_list:
        network_devices.append(driver_ios(hostname=device[0],
                                          username='ciscoadmin',
                                          password='!qAz@wSx#eDc'))

    devices_table = [['hostname', 'vendor', 'model', 'uptime',
                      'serial_number']]

    for device in network_devices:
        print("Connecting to {} ...".format(device.hostname))
        try:
            device.open()
            print("Getting device facts")
            device_facts = device.get_facts()
            devices_table.append(
                [
                    device_facts["hostname"],
                    device_facts["vendor"],
                    device_facts["model"],
                    device_facts["uptime"],
                    device_facts["serial_number"],
                ]
            )
        except:
            print(f"Non Cisco {device.hostname}")
            pass
        device.close()

    print("Done.")
    print(tabulate(devices_table, headers="firstrow"))
    print()


if __name__ == '__main__':
    main()
