class LogicGate:

    def __init__(self, n):
        self.label = n
        #self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        return self.perform_gate_logic()