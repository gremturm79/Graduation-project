from random import *

t = ['ab_1', 'ac_1', 'bc_2', 'bc_1']
a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in t if i[1] == 'c'}
print(a)
