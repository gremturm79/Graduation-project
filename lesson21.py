def such(tpl, s):
    for j in tpl:
        if s in tpl:
            return 'YES'
        else:
            return 'NO'


tpl1 = ('ab', 'abcd', 'cde', 'abc', 'def')
s1 = 'ab'
print(such(tpl1, s1))

tpl2 = [1, 2, 3, 4, 5]
s2 = 'f'
print(such(tpl2, s2))
