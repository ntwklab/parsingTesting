import textfsm
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

mrouteOutputNXOS = '''
IP Multicast Routing Table for VRF "default"

(*, 232.0.0.0/8), uptime: 3d00h, pim ip
  Incoming interface: Null, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 0)


(*, 239.0.1.2/32), uptime: 00:00:26, pim ip
  Incoming interface: loopback0, RPF nbr: 10.1.10.1
  Outgoing interface list: (count: 1)
    Ethernet1/2, uptime: 00:00:26, pim


(172.16.2.200/32, 239.0.1.2/32), uptime: 00:00:29, pim ip
  Incoming interface: Ethernet1/1, RPF nbr: 10.1.1.1, internal
  Outgoing interface list: (count: 0)


(*, 239.255.255.250/32), uptime: 1d08h, pim ip
  Incoming interface: loopback0, RPF nbr: 10.1.10.1
  Outgoing interface list: (count: 2)
    Ethernet1/2, uptime: 1d08h, pim
    Ethernet1/1, uptime: 1d08h, pim




'''

with open(basedir +'/nxos_mroute.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(mrouteOutputNXOS)

print(fsm.header)
print(result)


mrouteOutputIOS = '''
(*, 224.0.1.40), 1d07h/00:02:49, RP 10.1.1.1, flags: SL
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    GigabitEthernet0/1, Forward/Sparse, 1d07h/00:02:33

'''


