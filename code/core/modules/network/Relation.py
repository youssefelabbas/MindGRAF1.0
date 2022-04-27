
class Relation:
    name = ''
    type = ''
    adjust = ''
    limit = 0
    quantifier = False

    def __init__(self, n,  t,  a,  l):
        self.name = n
        self.type = t
        self.adjust = a
        self.limit = l
        self.setQuantifier()

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.limit = 1
        self.adjust = "none"
        self.setQuantifier()

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAdjust(self):
        return self.adjust

    def getLimit(self):
        return self.limit

    def isQuantifier(self):
        return self.quantifier

    def setQuantifier(self):
        self.quantifier = True
