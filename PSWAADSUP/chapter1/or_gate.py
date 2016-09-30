from binary_gate import BinaryGate


class OrGate(BinaryGate):

    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


g1 = OrGate("G1")
computed_value = g1.get_output()
print("The OR calculated value is %d." % computed_value)