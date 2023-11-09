from netmiko import ConnectHandler
import dev_connection
import os
from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
import json



templates = '/home/vanderson/.local/lib/python3.8/site-packages/ntc_templates/templates/'
os.environ['NET_TEXTFSM']= templates
#print(templates)

"""
Call function dev_connection that have all device and user information to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()
term_pager0 = net_connect.send_command('terminal pager 0')


cmd = net_connect.send_command(f'show interface', use_textfsm=True)
pprint(cmd)
#pprint(json.dumps(cmd))