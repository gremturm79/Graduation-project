import re

s = '5 + 7*2 - 4'
reg = r'\s*([+*-])\s*'
print(re.split(reg, s))
