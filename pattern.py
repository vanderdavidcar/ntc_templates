import re
import net_conn
from netmiko import ConnectHandler

iosv = net_conn.netmiko_nxos()
net_connect = ConnectHandler(**iosv)

show_int_nxos = net_connect.send_command('show ip int  brief | ex una')
pattern_intfnxos = "(\S+)\s+([\d\\.]+)\s+.protocol.(\S+)"
regex_intfnxos = re.findall(pattern_intfnxos,show_int_nxos)

show_intf_ios = net_connect.send_command('show ip int  brief | ex una')
pattern_intfios = "(\S+)\s+([\d\\.]+)\s+\w+.\w+\s.(up|administratively down)"
regex_intfios = re.findall(pattern_intfios,show_intf_ios)

show_vlanios = net_connect.send_command('show vlan brief | ex una')
pattern_vlanios = "(\d+)\s+(\S+)\s+(\S+)"
regex_vlanios = re.findall(pattern_vlanios, show_vlanios)
        
