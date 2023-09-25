import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def polska(s):
    stack = []
    lst = s.split()
    for i in srt:
        if i.isdigit():
           stack.append(i)
        else:
            
