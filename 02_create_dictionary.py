from netmiko import ConnectHandler
import net_conn
from dotenv import load_dotenv
import re
from pprint import pprint
from tabulate import tabulate
load_dotenv()

#places = ["spo", "bsa", "cta"]
places = ["bsa"]

for hosts in places: 
    #with open(f"devices_edge_mgmt.txt") as f:
    with open(f"devices_edge_{hosts}.txt") as f:
        devices_list = f.read().splitlines()
        print(devices_list)

    for devices in devices_list:
        print()
        print("#" * 79)
        iosv = net_conn.netmiko_nxos(devices)
        print(f'Connecting to device: {devices}')
    
        net_connect = ConnectHandler(**iosv)
        
        show_int_nxos = net_connect.send_command('show ip int  brief | ex una')
        pattern_intfnxos = "(\S+)\s+([\d\\.]+)\s+.protocol.(\S+)"
        regex_intfnxos = re.findall(pattern_intfnxos,show_int_nxos)

        show_intf_ios = net_connect.send_command('show ip int  brief | ex una')
        pattern_intfios = "(\S+)\s+([\d\\.]+)\s+\w+.\w+\s.(up|administratively down)"
        regex_intfios = re.findall(pattern_intfios,str(show_intf_ios))
        
        show_vlanios = net_connect.send_command('show vlan brief | ex una')
        pattern_vlanios = "(\d+)\s+(\S+)\s+(\S+)"
        regex_vlanios = re.findall(pattern_vlanios,show_vlanios)

        
        int_list = list()            
        
        for intface in regex_intfnxos:
            
            int_dict = dict()
            int_list.append(int_dict)
            
            #int_dict['vlan'], int_dict['name'], int_dict['status']= intface[0], intface[1], intface[2] # Vlan
            int_dict['intf'], int_dict['ip'], int_dict['status'] = intface[0], intface[1], intface[2] # Interfaces
        
        print(tabulate(int_list, headers='keys', tablefmt='grid'))