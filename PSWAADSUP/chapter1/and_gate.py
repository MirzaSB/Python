from binary_gate import BinaryGate


class AndGate(BinaryGate):

    def __init__(self, n):
        super(AndGate, self).__init__(n)
        self.gate_type = "AND"

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


#g1 = AndGate("G1")
#computed_value = g1.get_output()
#print("The AND calculated value is %d." % computed_value)