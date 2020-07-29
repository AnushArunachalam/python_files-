# # def cube(x):
# #     return x**3      # return == stop
# # print(cube(2))


# # def calculators(a, s, m):
# #     return a+s+m, a-s-m, a*s*m
# # print(calculators(1, 2, 3))

# # def check_if_present(a, b):
# #     for s in a:
# #         if s == b:
# #             return True
# #     else:
# #         return False
# # print(check_if_present({"anush", "vijay", "karthick"}, "vijay")) 

# # def name(x, y):
# #     return dict(zip(x, y))
# # print(name(["rajini", "kamal", "vijay"], ["kaala", "indian", "master"]))

def funct(h):
    return set(h)
print(funct("hello"))


# def fun(f, j):
#     if isinstance(f, str) and f.isupper():
#         return f.lower()
#     if isinstance(j, str) and j.isupper():
#         return j.lower()
#     else:
#         return f.upper(), j.upper()
# print(fun("ANUSH", "AMERICA"))        

# def fun(f, j):
#     if isinstance(f, str) and isinstance(j, str) and f.isupper() and j.isupper():
#         return f.lower(), j.lower()
#     else:
#         return f, j
# print(fun("anush", "AMERICA"))  