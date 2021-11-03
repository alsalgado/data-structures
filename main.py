from multipleArrayList import List

lista = List()

print(f'''
Primeira lista:

next: {lista.next}
key: {lista.key}
prev: {lista.prev}''')

lista.insert(1)

print(f'''
Segunda lista:

next: {lista.next}
key: {lista.key}
prev: {lista.prev}''')

lista.insert(2)

print(f'''
Terceira lista:

next: {lista.next}
key: {lista.key}
prev: {lista.prev}''')


lista.insert(16)

print(f'''
Quarta lista:

next: {lista.next}
key: {lista.key}
prev: {lista.prev}''')


busca = lista.search(2)

print(f'''
Primeira busca:

resposta: {busca}
item: {lista.key[busca]}''')

lista.delete(2)

print(f'''
Primeira deleção:

Item deletado: 2

next: {lista.next}
key: {lista.key}
prev: {lista.prev}''')
