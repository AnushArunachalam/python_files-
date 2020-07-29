
'''

lambda is also known as anynonyms function
throw away function.


'''


lis = [1, 2, 3, 4, 5]

x = list(map(lambda a: a ** 2, lis))

# map > (function, iterable)
# lambda expression > parameter 


# 

print(x)


def func(a):

    return list(map(lambda a: a ** 2, a))


print(func([1, 2, 3, 4, 5]))


''''

lambda parameter: expression
 
lists = [10, 20, 30, 40, 59]
g = list(map(lambda x, y: x + y , lists))
print(g)



'''
lists1 = [10, 20, 30, 40, 59]
lists2 = [120, 134, 457,474,2247]
g = list(map(lambda x, y: x * y , lists1, lists2))
print(g)

