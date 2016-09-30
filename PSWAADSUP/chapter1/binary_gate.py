from logic_gate import LogicGate


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input("Enter Pin A input for gate " + self.get_label() + " ---> "))

    def get_pin_b(self):
        return int(input("Enter Pin B input for gate " + self.get_label() + " ---> "))
