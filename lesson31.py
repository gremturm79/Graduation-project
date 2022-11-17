import math


def sqr(figure_type, **kwargs):
    if figure_type == 'rhombus':
        return print(kwargs['d1'] * kwargs['d2'] / 2)
    elif figure_type == 'square':
        return print(kwargs['a'] * kwargs['a'])
    elif figure_type == 'trapezoid':
        return print((kwargs['a'] + kwargs['b']) * kwargs['h'] * 0.5)
    elif figure_type == 'circle':
        return print(math.pi * kwargs['r'] ** 2)
    elif figure_type == 'unknown':
        return print('invalid data')


sqr(figure_type='rhombus', d1=10, d2=8)
sqr(figure_type='square', a=5)
sqr(figure_type='trapezoid', a=12, b=3, h=6)
sqr(figure_type='circle', r=18)
sqr(figure_type='unknown', a=1, b=2, c=3)
