'''
Task 2

Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,

`end`, and optional step. Tips: See the documentation for `range` function

1 - проверка как оно работает

2 - Concatenation of two range() functions using itertools

'''

for i in range(18, -1, -3):
    print(i, end=" ",)

from itertools import chain

res = chain(range(5), range(10,20,3))
for x in res:
    print("\n", x, end=" ")
