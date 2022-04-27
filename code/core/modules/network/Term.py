
class Term:
    identifier = None
    temp = False
    upcableset = None

    def __init__(self, idenitifier):
        self.identifier = idenitifier
        self.temp = False

    def getIdentifier(self):
        return self.identifier

    def isTemp(self):
        return self.temp

    def setTemp(self, temp):
        self.temp = temp
