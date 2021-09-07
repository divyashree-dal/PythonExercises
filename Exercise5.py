class InputOutString:
    def __init__(self):
        self.s=''
    def getString(self):
        self.s = raw_input("Enter a string")
    def printString(self):
        print self.s.upper()

inout = InputOutString()
inout.getString()
inout.printString()