from logic_gate import LogicGate


class UnaryGate(LogicGate):

    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter Pin input for the " + self.gate_type
                         + " gate " + self.get_label() + " ---> "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS at Unary Gate level")