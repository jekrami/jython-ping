#!/usr/bin/python
import napalm
from tabulate import tabulate


def main():

    driver_ios = napalm.get_network_driver('ios')

    device_list = [['192.168.155.2', 'ios', 'core-switch'],
                   ['192.168.155.161', 'ios', 'router']]

    network_devices = []
    for device in device_list:
        network_devices.append(driver_ios(hostname=device[0],
                               username='ciscoadmin',
                               password='!qAz@wSx#eDc'))

    devices_table = [['hostname', 'vendor', 'model', 'uptime',
                     'serial_number']]

    try:
        for device in network_devices:
            print ('Connecting to {} ...'.format(device.hostname))
            device.open()
            print ('Getting device facts')
            device_facts = device.get_facts()
            devices_table.append([device_facts['hostname'],
                                 device_facts['vendor'],
                                 device_facts['model'],
                                 device_facts['uptime'],
                                 device_facts['serial_number']])

        device.close()
    except:
        print(f"Non Cisco {device.hostname}")
        pass

    print ('Done.')
    print (tabulate(devices_table, headers='firstrow'))
    print ()


if __name__ == '__main__':
    main()
