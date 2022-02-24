# Tuples

tuple_x = (1, 2, 4)
# tuple[2] = 4 can't do that

list_s = [2, 'asd', 5, ',lol']
print(list_s)

(x, y) = (3, 'lol')

if (4, 2, 5) > (2, 3, 1):
    print("yes")

d = {'b' : 2, 'a' : 11, 'c' : 6}
temp = list()
for k, v in sorted(d.items()):
    print(k, v)
    temp.append((k, v))

temp = sorted(temp, reverse=True)
print(temp)

for key, value in temp[:2]:
    print(key, value)

print( sorted( [ (k, v) for k, v in d.items() ] ) )

x, y = 3, 4
print("y = ", y)

x = {"lol":1, "bob":2, "sos": 3}
y = x.items()
print(type(y))
print(dir(y))
for elem in y:
    print(elem)