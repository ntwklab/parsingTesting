import textfsm
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

mrouteOutputNXOS = '''
IP Multicast Routing Table for VRF "default"
IP Multicast Routing Table for VRF "default"
IP Multicast Routing Table for VRF "default"
IP Multicast Routing Table for VRF "default"

(0.0.0.0/32, 239.255.255.250/32), uptime: 1d08h, pim ip
  Incoming interface: loopback0, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 2)
    Ethernet1/0, uptime: 1d08h, pim
    Ethernet1/0, uptime: 1d08h, pim

(*, 239.255.255.250/32), uptime: 1d08h, pim ip
  Incoming interface: loopback0, RPF nbr: 1.1.1.1
  Outgoing interface list: (count: 2)
    Ethernet1/1, uptime: 1d08h, pim
    Ethernet1/2, uptime: 1d08h, pim

(1.1.1.1/32, 239.255.255.250/32), uptime: 1d08h, pim ip
  Incoming interface: loopback0, RPF nbr: 2.2.2.2
  Outgoing interface list: (count: 2)
    Ethernet1/3, uptime: 1d08h, pim
    Ethernet1/4, uptime: 1d08h, pim


'''

with open(basedir +'/nxos_mroute.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(mrouteOutputNXOS)

print(fsm.header)
for r in result:
    print(r)
