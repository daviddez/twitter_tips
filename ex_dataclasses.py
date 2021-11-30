"""
Save time when writing Python classes -  data classes reduce the amount of boiler plate code 
required when writing classes. By default a data class will generate the special methods init, 
repr, str and eq for you.
https://www.packetcoders.io/save-time-when-writing-python-classes/
"""

from dataclasses import dataclass

@dataclass
class Interface:
    name: str
    speed: int
    mtu: int

rtr_Interface = Interface(name="gi0/1", speed="1000", mtu="1500")

print(rtr_Interface)
print(type(rtr_Interface))

print(rtr_Interface == rtr_Interface)
