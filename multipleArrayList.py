'''
Lista duplamente encadeada implementada sem ponteiros usando múltiplos arrays
'''
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = []
        self.key = []
        self.prev = []

    def insert(self, elem):
        if self.head==None:
            self.key.append(elem)
            self.next.append(None)
            self.prev.append(None)
            self.head = 0
            self.tail = 0
        else:
            self.key.append(elem)
            self.next.append(self.head)
            self.prev.append(None)
            self.prev[self.head] = self.head + 1
            self.head +=1
            

    def search(self, elem):
        x = self.head
        while x and self.key[x]!=elem:
            x=self.next[x]
        return x

    def delete(self, elem):
        x = self.search(elem)
        if self.prev[x] != None:
            self.next[self.prev[x]] = self.next[x]
        else:
            self.head = self.next[x]
        if self.next[x] != None:
            self.prev[self.next[x]] = self.prev[x]
        self.key[x] = 'garbage collector'
        self.next[x] = 'garbage collector'
        self.prev[x] = 'garbage collector'