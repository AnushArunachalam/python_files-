list comprehension

l = ['john', 'david', 'savanna', 'george']

for i in l:

    print(i)

lis = ['amanda', 'david', 'stephen', 'tim']
l = [x[0] for x in lis]
print(l)

def square(n):

    return n**2

x = square(10)
print(x)

an = [yd**2 for yd in range(1, 11) if yd %2 != 0 ]
print(an)


dictionary comprension
l1 = ['Sachin', 'Beckham', 'Anand']
l2 = ['Cricket', 'Football', 'chess']
d = {ad:am for ad,am in zip(l1,l2)}

print(d)