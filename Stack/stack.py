# Implementação da classe Pilha usando Python
class Stack:
    def __init__(self, elems = []):
        self.elems = elems
        self.top = None
        self.updateTop()

    def push(self, elem):
        self.elems.append(elem)
        self.updateTop()

    def pop(self):
        if self.isEmpty():
            print('Pilha vazia')
        else:
            self.elems.pop()
            self.updateTop()
    
    def isEmpty(self):
        if not self.elems:
            return True
        return False

    def updateTop(self):
        if self.isEmpty():
            self.top = None
        else:
            self.top = len(self.elems) - 1

