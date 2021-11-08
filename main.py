# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.suc = None

    def view(self):
        """
        Imprime as informações do nó.
        """
        print(f"""
        |> Data: {self.data} | Type: {type(self.data)} 
        |> Predecessor -> {self.pre if self.pre == None else self.pre.data}
        |> Successor -> {self.suc if self.suc == None else self.suc.data}
        """)


class DoublyLinkedList:
    def __init__(self):
        self.ini = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        """
        Verifica se a lista está vazia.
        """
        if self.ini == None: return True
        else: return False

    def headInsert(self, data):
        """
        Insere no início da lista.
        """
        node = Node(data)
        if self.isEmpty():
            self.ini = node
            self.end = node

        else:
            node.suc = self.ini
            self.ini.pre = node
            self.ini = node

        self.size += 1
        
    def tailInsert(self, data):
        """
        Insere no fim da lista.
        """
        node = Node(data)
        if self.isEmpty():
            self.ini = node
            self.end = node

        else:
            node.pre = self.end
            self.end.suc = node
            self.end = node

        self.size += 1

    def headDelete(self):
        """
        Remove o primeiro item da lista.
        """
        if not self.isEmpty():
            self.ini = self.ini.suc
            self.ini.pre = None
            self.size -= 1

    def tailDelete(self):
        """
        Remove o último item da lista.
        """
        if not self.isEmpty():
            self.end = self.end.pre
            self.end.suc = None
            self.size -= 1

    def insert(self, data, index):
        """
        Insere um item em um determinado índice da lista.
        """
        if not self.isEmpty():
            if index == 0: self.headInsert(data)
            elif index == self.size - 1: self.tailInsert(data)
            elif index < 0 or index > self.size - 1: print("\n[!] INSERTION ERROR.")
            else:
                node = Node(data)
                aux = self.ini
                listIndex = 0

                while(listIndex != index):
                    aux = aux.suc
                    listIndex += 1

                node.suc = aux
                node.pre = aux.pre
                node.pre.suc = node
                aux.pre = node

                self.size += 1

    def delete(self, index):
        """
        Remove um item por um determinado índice da lista.
        """
        if not self.isEmpty():
            if index == 0: self.headDelete()
            elif index == self.size - 1: self.tailDelete()
            elif index < 0 or index > self.size - 1: print("\n[!] DELETION ERROR.")
            else:
                aux = self.ini
                listIndex = 0

                while(listIndex != index):
                    aux = aux.suc
                    listIndex += 1

                aux.pre.suc = aux.suc
                aux.suc.pre = aux.pre

                self.size -= 1

    def searchByIndex(self, index):
        """
        Pesquisa um item na lista pelo índice.
        """
        if not self.isEmpty():
            if index == 0: return self.ini.data
            elif index == self.size - 1: return self.end.data
            elif index < 0 or index > self.size - 1: print("\n[!] NOT FOUND.")
            else:
                aux = self.ini
                listIndex = 0

                while(listIndex != index):
                    aux = aux.suc
                    listIndex += 1

                return aux.data

                

    def searchByItem(self, item):
        """
        Pesquisa o índice de um item da lista.
        """
        if not self.isEmpty():
            if item == self.ini.data: return 0
            elif item == self.end.data: return self.size - 1
            else:
                aux = self.ini
                itemIndex = 0

                while(item != aux.data and aux.suc != None):
                    aux = aux.suc
                    itemIndex += 1

                if itemIndex == self.size - 1: print("\n[!] NOT FOUND.")
                else: return itemIndex

    def view(self):
        """
        Imprime os nós da lista.
        """
        print(f"\n\n[*] LIST SIZE: {self.size}")

        aux = self.ini
        while(aux != None):
            aux.view()
            aux = aux.suc
        

lst = DoublyLinkedList()
lst.headInsert(0)
lst.tailInsert([1, 2, 3])
lst.tailInsert((4, 5, 6))
lst.tailInsert(4.8)
lst.tailInsert({"a":"1", "b":"2", "c":"3"})
lst.headInsert("abc")
lst.view()

lst.headDelete()
lst.tailDelete()
lst.view()

lst.insert(True, 1)
lst.delete(4)
lst.view()

print(lst.searchByItem((4, 5, 6)))
print(lst.searchByIndex(1))
