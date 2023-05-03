tpl = tuple((1, 2, 4, 8, 6, 4, 1, 8, 5, 2))
x = 8
for i in range(len(tpl)):
    if tpl.count(x) == 0:
        tpl = list(tpl)
        del tpl[0:len(tpl)+1]
        tpl = tuple(tpl)
        print(tuple(tpl))
        break
    if tpl[i] == x and tpl.count(x) == 1:
        print(tpl[i:])
        break
    if tpl[i] == x and tpl.count(x) == 2:
        index1 = tpl.index(x)
        index2 = tpl.index(x, index1+1)
        print(tpl[index1:index2+1])
        break



