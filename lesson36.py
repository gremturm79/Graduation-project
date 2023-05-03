res = (lambda a: (lambda b: (lambda c: a * b * c)))(2)(5)(5)
print(res)

nums = [3, 5, 7, 3, 9, 5, 7, 2]


res3 = (lambda x, y, z: x * y * z)
print(res3(2, 5, 5))


res1 = list(map(lambda x: x ** 2, nums))
print(res1)

res2 = list(map(lambda x: x ** 3, nums))
print(res2)
