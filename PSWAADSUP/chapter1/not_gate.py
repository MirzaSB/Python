from unary_gate import UnaryGate


class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n)
        self.gate_type = "NOT"

    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 0:
            return 1
        else:
            return 0

'''
g1 = NotGate("G1")
computed_value = g1.get_output()
print("The NOT calculated value is %d." % computed_value)
'''