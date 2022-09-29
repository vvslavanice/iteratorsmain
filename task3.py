'''
Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic
for retrieving elements using square brackets syntax.
'''
'''

First TRY 

'''
class Iteratorwithiterables:

    def __init__(self, iterable: str, ind = 0):
        self.iterable = iterable
        self.ind = ind

    def iter(self):
        return self

    def __next__(self):
        if self.ind == len(self.iterable): '''ТАК ДЕЛАТЬ НЕЛЬЗЯ, НЕ МОЖЕТ ТАКОГО БЫТЬ !'''
            prvs_ind == self.ind
            self.ind += 2
            return len(self.iterable[prvs_ind:])
        else:
            raise StopIteration

if __name__ == '__main__':
    smth = Iteratorwithiterables("something", 2)
    for i in smth:
        print(i)


'''
Second TRY
'''

class Iteratorwithiterables:

    def __init__(self, iterable: str, index=0):
        self.iterable = iterable
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            old_index = self.index
            self.index += 1
            return len(self.iterable[old_index:])
        else:
            raise StopIteration

if __name__ == '__main__':
    smth = Iteratorwithiterables("skolko", 3)
    for i in smth:
        print(i)