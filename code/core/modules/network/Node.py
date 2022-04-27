
from syntactic.Term import Term
from semantic.Entity import Entity


class Node:

    syntactic = Term()
    semantic = Entity()
    id = ""
    count = 0
    name = ""
    supports = set()
    downCableS = DownCableSet

    def __init__(self, synt, sem, count, id):
        self.syntactic = synt
        self.semantic = sem
        self.id = id
        self.count = count
        id = count
        count += 1

    def __init__(self, synt, sem, count, id, name):
        # instance of the class with the specified class name
        self.id = id
        self.count = count
        id = count
        count += 1
# creation of the molecular node

    def __init__(self, synt, sem, count, id, name, downCableS):
        # instance of the class with the specified class name
        # the downcable set of the molecular node ,will use an instance of the syntactic class
        self.id = id
        self.count = count
        id = count
        count += 1

    def getname(self):
        # print("getter method called")
        return self.name

    def getsupports(self):
        return self.support

    def getid(self):
        return self.id

    def getcount(self):
        return self.count

    def setcount(self, count):
        self.count = count

    def setid(self, id):
        self.id = id

    def isTemp():
        return Term.isTemp()

    def isTemp(temp):
        Term.setTemp = temp

    def __init__(term):
        term.Term

    def getsyntactic(self):
        return self.syntactic

    def getsemantic(self):
        return self.semantic

    def getidentifier(self):
        return self.syntactic.getIdentifier
