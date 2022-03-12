# class examples

myL = [('a', 3), ('b', 2), ('f', 1), ('d', 1), ('e', 1), ('c', 0)]
CDCdata = {'King': {'Mar': 2706, 'Apr': 3620, 'May': 1860, 'Jun': 2157, 'July': 5014, 'Aug': 4327, 'Sep': 2843},
           'Pierce': {'Mar': 460, 'Apr': 965, 'May': 522, 'Jun': 647, 'July': 2470, 'Aug': 1776, 'Sep': 1266},
           'Snohomish': {'Mar': 1301, 'Apr': 1145, 'May': 532, 'Jun': 568, 'July': 1540, 'Aug': 1134, 'Sep': 811},
           'Spokane': {'Mar': 147, 'Apr': 222, 'May': 233, 'Jun': 794, 'July': 2412, 'Aug': 1530, 'Sep': 1751},
           'Whitman': {'Apr': 7, 'May': 5, 'Jun': 19, 'July': 51, 'Aug': 514, 'Sep': 732, 'Oct': 278}}
print((CDCdata.values()))
v = CDCdata.values()

sorted(myL)

# a lambda representation of the same function would be
sorted(myL, key=lambda item: item[1])


# histogram
def histo(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return sorted(sorted(list(d.items())), key=lambda item: item[1], reverse=True)


# class examples generator versiin
def letters(start, finish):
    current = start
    while current == finish:
        print("before yield")
        yield current
        print("after yield")
        current = chr(ord(current) + 1)


gletters = letters("a", "d")
for c in gletters:
    c.next()


# iterator version-- look at the slide and finsih this before starting to work on the homework
def letters():
    return


# stream-- finish this as well its not related to any of the assignments but it is a good thing to understand especially for the linked list data structure

a = [('e', 3), ('m', 2)]
b = dict(a)
print(b)


# this is the definition of a n iterator. This is what it does under the hood.
class copyIter2(object):
    def __init__(self, it):
        self.input1 = it
        try:
            self.current = self.input1.__next__()
        except:
            self.current = None

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        try:
            self.current = self.input1.__next__()
        except:
            self.current = None
        return result

    def __iter__(self):
        return self


# higher order functions
# map
def map(f, alist):
    answer = []
    for v in alist:  # generate each value v in a list
        answer.append(f(v))  # put (v) in a list to return
    return answer


# filter
def filter(p, alist):
    answer = []
    for v in alist:
        if p(v):
            answer.append(v)
    return answer
#reduce (foldr in haskell)

