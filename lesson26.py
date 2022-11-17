a = {1: 10, 2: 20}
b = {2: 30, 3: 40}
c = {4: 50, 5: 60, 6: [1, 2]}
c1 = {'one': {'two': 2}}
d = a | b | c
print('1 способ', d)
e = dict()
e.update(a)
e.update(b)
e.update(c)
print('2 способ', e)

dict1 = {}
for key, value in a.items():
    dict1[key] = value
for key, value in b.items():
    dict1[key] = value
for key, value in c.items():
    dict1[key] = value

print('3 способ', dict1)

# dict2 = {}
dict2 = {**dict1, **c1}
print('4 способ', dict2)


def gen_dict(diction):
    for key, value in diction.items():
        dict1[key] = value
        return dict1


print(gen_dict(dict1))

