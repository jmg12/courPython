# /usr/bin/python

'''def fact (n):
    if n == 0:
        return 1
    return n * fact(n-1)
'''
def _fact(n, p):
    if n == 0:
        return p
    # p * n! == p * n * (n - 1)!  
    return _fact(n * _fact(n - 1 ,p * n)
    # return p * n!

def fact(n):
    return _fact(n, 1)


print(fact(3))
