from Pilha import Pilha

from random import  randint

pilha = Pilha(10)

for i in range(10):
    pilha.push(randint(0, 100))

print(pilha)
print(pilha.top)
pilha.pop()

print(pilha)
print(pilha.top)

print(pilha)

print(reversed(pilha))