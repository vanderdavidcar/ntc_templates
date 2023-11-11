from netmiko import ConnectHandler
import net_conn
from dotenv import load_dotenv
import csv
load_dotenv()

"""
This is a way to create a csv file retrieving data from many devices
"""

with open(f"devices_edge_bsa.txt") as f:
    devices_list = f.read().splitlines()
    print(devices_list)

    for devices in devices_list:
        print()
        print("#" * 79)
        iosv = net_conn.netmiko_nxos(devices)
        print(f'Connecting to device: {devices}')
    
        net_connect = ConnectHandler(**iosv)
        print()

        """
        Devices Information
        """
        show_ver = net_connect.send_command('show version', use_textfsm=True)

        for data in show_ver:
            version = show_ver[0].keys()
            # Dictionary
            print(f"Hostname: {data['hostname']}")
            print(f"Uptime: {data['uptime']}")
            print(f"OS: {data['os']}")
            print(f"Platform: {data['platform']}")
            print(f"SN: {data['serial']}")
        
            with open(f'log.csv', 'a') as out_file:
                writer = csv.DictWriter(out_file, fieldnames=version)
                writer.writeheader()
                writer.writerow(data)

        """
        How many vlans are configured on devices
        """
        
        show_vlan = net_connect.send_command('show vlan brief', use_textfsm=True)

        for data_vlan in show_vlan:
                vlans = show_vlan[0].keys()
             
                # Dictionary
                print(f"\nVlan ID: {data_vlan['vlan_id']}")
                print(f"Name: {data_vlan['name']}")
                print(f"Status: {data_vlan['status']}\n")
        
        """
        All routing tables configured on devices
        """
        
        show_route = net_connect.send_command('show ip route', use_textfsm=True)

        for data_route in show_route:
                route = show_route[0].keys()
                
                # Dictionary
                print(f"\nVRF: {data_route['vrf']}")
                print(f"Protocol: {data_route['protocol']}")
                print(f"Network: {data_route['network']}/{data_route['mask']}")
                print(f"Next-hop: {data_route['nexthop_ip']}")
                print(f"Uptime: {data_route['uptime']}\n")