def info(**kwargs):
    my_dict.update(kwargs)
    return my_dict


my_dict = {'first': 'one'}
print(info(k1=22, k2=31, k3=11, k4=91))
print(info(name='Bob', age=31, weight=61, eyes_color='grey'))
