from scrapli.driver.core import IOSXEDriver, NXOSDriver
from scrapli.helper import textfsm_parse
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 


class CiscoCommands:

    def __init__(self):
        self.username = 'admin'
        self.password = 'Stefan2020'


    def conn(self, ip):

        switch = {
            "host": ip,
            "auth_username":self.username,
            "auth_password":self.password,
            "auth_strict_key":False,
            # "auth_bypass": True,
            "transport": "paramiko",
            "timeout_ops": 2, 
            "timeout_socket": 1, 
            "timeout_transport": 1
        }

        try: 
            host = IOSXEDriver(**switch)
            host.open()
            os = "ios"

        except:
            host = NXOSDriver(**switch)
            host.open()
            os = "nxos"

        return host, os


    def show_mroute(self, q):
        ip = q

        # Check IOS Type   
        host, os = CiscoCommands.conn(self, ip)
        print(f"host: {host}, OS: {os}")

        # Show interface details
        if os == "ios":
            print("I am IOS and running IOS command")
            output = host.send_command("show ip mroute")
        elif os == "nxos":
            print("I am Nexus and running Nexus command")
            output = host.send_command("show ip mroute")

        # TextFSM parse response
        textfsm_template = basedir +'/nxos_mroute.textfsm'
        textfsm_parsed_response = textfsm_parse(textfsm_template, output.result,)

        for line in textfsm_parsed_response:
            print(line)


if __name__ == '__main__':
    q = "172.16.1.115"

    self = CiscoCommands()
    error_ips = CiscoCommands.show_mroute(self, q)
