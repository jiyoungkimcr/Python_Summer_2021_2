# Tuples
li1 = [1, 0, 4654, 4]
li2 = [3, 6, 4, 21]
li3 = [li1, li2]
print(li3)
print(li3[0][2])

t1 = (14, 15)
t2 = (24, 243, 54)
print(t2[1])

a, b, c = t2
print(a)
print(b)
print(c)

#tuples, useful when you want to return multiple values from the function
#tuples are 'not changeable' (cannot append, delete, or add)


#Dictionary
# what's important about Dictionary?, what's the limitation?
# the key should be unique (value doesn't need to be)

print()
d1 = { 'a': 10, 'b': 11, 'c': 12}
#d1 = {'a': 10, 'b': 11, 'c': 12, 'a': 45} <- this will not work since every key should be unique

print(d1['a'])

print(list(d1.values()))

print(list(d1.keys()))

for key in d1.keys():
    print(d1[key])