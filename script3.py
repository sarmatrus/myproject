a = [1, 2, 3]
b = a
a.append(4)
objects = [1, 2, 1, 2, 3, a, b, True, True, False, 0, 0, 1, 2, [1, 2]]
objectsn = list(map(id, objects))
d = set(objectsn)
print(len(d))
