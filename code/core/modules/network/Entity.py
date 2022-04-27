
from LinkedList import LinkedList


class Entity():
    entityType = None
    superClass = None
    act = None
    proposition = None

    def __init__(self, entity):
        self.entityType = entity
        self.superClass = None

    def __init__(self, entity, superClass):
        self.entityType = entity
        self.superClass = superClass

    def getSuperClassesNames(self):
        superClassesNames = LinkedList()
        return superClassesNames

    def getEntityType(self):
        return self.entityType
