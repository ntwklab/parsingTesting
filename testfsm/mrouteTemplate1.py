import textfsm
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

mrouteOutput = '''
(*, 224.0.1.40), 00:00:12/00:02:48, RP 0.0.0.0, flags: DCL
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    Loopback0, Forward/Sparse, 00:00:11/00:02:48
'''

with open(basedir +'/mroute.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(mrouteOutput)

print(fsm.header)
print(result)
