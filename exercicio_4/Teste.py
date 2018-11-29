from Deque import Deque
from random import randint

deque = Deque(5)

for i in range(5):
    deque.push_front(randint(0, 100))


print(deque)

print(deque.peek_front())
print(deque.peek_back())

print("Final:")
print(deque)
print(deque.pop_back())
print(deque)


print("Começo:")
print(deque)
print(deque.pop_first())
print(deque)
