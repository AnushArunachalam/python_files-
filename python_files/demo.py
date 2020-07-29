# INT COMMON OPERATION
number = 2000 # immutable data-type

# print(number[0]) # indexing means [], not possible to grab anything int datatype, int does not support indexing

convert = str(number) # type conversion, converting int to str
# print(type(convert))


# for index in number: > iteration is not possible, int does not support iteration
#     print(index)

# print(id(number)) 

number = 1000

# print(id(number))

# STRING COMMON OPERATION

text = "somename" # immutable data type

# print(text) 

# print(text[0]) # indexing is possible [] in str data type

# print(text[::-1]) # beginner reversal

# text[0] = "h"

# print(text)

# join()

# print("-".join(text)) # average implementation
 
# delimiter = "-" # ok!

# print(delimiter.join(text))


# ls = "*".join(text) # joins any character or a symbol to the string.
# print(ls.replace("*", "#")) # actual existing character, your custom change

# word = "abracadabra"
# count_each_word = word.count("a") 
# print(count_each_word)

# txt = "world"

# print(txt.endswith("d")) # returns a boolean value, True or False

# txt = "hello world       "

# print(txt.strip()) # removes any trailing white-spaces in a string



# LIST COMMON OPERATIONS # Mutable data type

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # 2504582758208 

l2 = list(range(110, 210, 10)) # print list from 100 to 200 from step size 10

l3 = l1 + l2 # concatination is possible> we can combine two lists together

# # print(l3)
# print(id(l3))
# l3.append(210)
# print(l3)
# print(id(l3))

# print(f'before change > {l3}')
# l3[3] = "random" # assignment 

# print(l3[4]) # indexing is possible


# l4 = dict(zip("python", range(1, 7)))
# print(l4)

# l3.extend(l4.items())

# print(l3)


# pop = l3.pop() # pop removes last element from list
# print(pop)
# print(l3)


# idx = l3.index(190) # retrieve index value of a particular element
# print(idx)


# l1.insert(9, "hello") # add "hello" at index 9, and the existing value will be shifted to next index.
# print(l1)

# cpy = l1.copy() # copies the list

# print(cpy)




# def func(lis, dic, string):

#     print(lis[0])
#     print(dic.values())
#     print(string[::-1])

# a = [100, 200, 300, 400]
# b = {'a': 100, 'b': 200, 'c': 300}
# c = "anush"

# func(a, b, c)

# import requests

# def func(response):

#     if requests.get(response):         # 25
#         return True
#     else:
#         return False

# res = func("https://python.org")

# print(res)

# TUPLE DATATYPE > IMMUTABLE

t = (10, 20, 30) # object state will not be changed
# print(type(t), t)

# t[1] = 30 # item assignment is not possible 

# print(t[1]) # indexing is possible.

# cnt = ("fjkhjksdfghndrtnfdhnckhnr")

# print(cnt.index("j"))


# Dictionary mutuable

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(a=100, b=200, c=300)
d3 = dict(zip("python", range(1, 7)))

# print(d1, type(d1))
# print(d2, type(d2))
# print(d3, type(d3))

# grab = d1["a"]

# print(grab)

# d1["a"] = [10, 20, 30] # assignment is possible

# print(d1)

# for i in d1.items():    # keys(), values()
#     print(i)


# print(d1.get("a")) # retrieve value from the specified key


# set immutable data type # no duplicates, order of insertion will not be maintained.

s = {10, 20, 30, 40, 50, 50}

# print(s[0]) indexing is not possible

# s.remove(10)  

# s[0] = 1000 # assignment is not possible

# print(s)







