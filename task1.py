'''
Task 1

Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:

`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

1 - просто проверка как оно работает
2 - немного попытался поиграть с функцией и if функцией
'''

Monthes = ["January", "February", "March"]
enummonthes = enumerate(Monthes, 0)

print(list(enummonthes))


letters = ['s', 'l', 'a', 'v', 'a']
def with_index(iterable, start = 0):
    x = start
    for elem in iterable:
        yield x, elem
        x += 1
    if x >= 10:
        print('It should be not like that')
    else:
        print("Everything fine")
    return x

for n in with_index(letters, 1):
    print(n)