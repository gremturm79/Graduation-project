import re


def password(word):
    return re.findall(r'^[-\dA-z@_]{6,18}$', word)


print((password('my-p@sswOrd')))
print((password('#my-p@sswOrdФ')))
print((password('my-p@s%swOrd')))

