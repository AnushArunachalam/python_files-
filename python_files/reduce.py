# today we take a look at a function called reduce()

# this reduce function is available in functools package

from functools import reduce

# above we have imported reduce function from functools

lis = [10, 20, 30, 40, 50]

lis_str = ['anush', 'arunachalam']

# What if i want to add all the elements inside this list?
# we can use reduce function to do this task.

# like map and filter function, reduce also takes 2 parameters.
# 1st parameter is a function, second parameter is an iterable.
result = reduce(lambda x, y: x+y, lis) # it basically adds left and right hand elements.
 # this one use case.

# we can simplify this. 

import operator # this is called package. inside this we have n number of classes and functions.


# result = reduce(lambda x, y: x+y, lis_str) this one is bit complicated.

# higher order function

'''
zip takes 2 iterables
reduce - function, iterable
filter
map
'''


l1 = [10, 20, 30, 40]

l2 = ['ten', 'twenty', 'thirty', 'fourty']

d = dict(zip(l1, l2))

print(d)

r = reduce(operator.pow, lis)


def func(x):

    return x[0]

fun = map(func, 'string')
print(list(fun))