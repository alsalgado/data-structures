class Queue:
    def __init__(self, elems = []):
        self.elems = elems
        self.head = None
        self.tail = None
        self.updateHeadTail()

    def enqueue(self, elem):
        self.elems.append(elem)
        self.updateHeadTail()

    def dequeue(self):
        if self.isEmpty():
            print('Fila vazia')
        else:
            self.elems.pop(0)
            self.updateHeadTail()

    def isEmpty(self):
        if self.elems:
            return False
        return True
    
    def updateHeadTail(self):
        if self.isEmpty():
            self.head = None
            self.tail = None
        else:
            self.head = 0
            self.tail = -1
    