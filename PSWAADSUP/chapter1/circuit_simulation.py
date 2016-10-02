from and_gate import AndGate
from or_gate import OrGate
from not_gate import NotGate
from connector import Connector


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

#g3.get_output()
z = g4.get_output()
print(z)