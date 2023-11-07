from netmiko import ConnectHandler
from getpass import getpass
import net_conn
from dotenv import load_dotenv
from pprint import pprint
import textfsm
import csv
load_dotenv()

with open(f"hosts.cfg") as f:
    hosts = f.read().splitlines()
    print(hosts)

for devices in hosts: 
        print()
        print("#" * 79)
        iosv = net_conn.netmiko_nxos(devices)
        print(f'Connecting to device: {devices}')
    
        net_connect = ConnectHandler(**iosv)
        print()
        command1 = net_connect.send_command('show vlan brief', use_textfsm=True)

        for i in command1:
            new = []
            new.append(i)

            for data in new:
                list_of_devices = command1[0].keys()
             
                # Dictionary
                print(f"Vlan ID: {data['vlan_id']}")
                print(f"Name: {data['name']}")
                print(f"Status: {data['status']}")
                print(f"Interfaces: {data['interfaces']}\n")

                """
                Note: Needed to split all data to columm after comma in excel. 

                Select first columm > Data > Text to Columm > Delimeted > Comma/Semicomma > Finish

                """            
   
                with open(f'{devices}.csv', 'a', newline='') as out_file:
                    writer = csv.DictWriter(out_file, fieldnames=list_of_devices)
                    writer.writeheader()
                    writer.writerow(data)

    