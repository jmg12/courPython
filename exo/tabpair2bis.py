# /usr/bin/python

'''Passer à la fonction un nb arbitraire d'argument et mettre dans un tuble.
Le corp de la fonction est un tuple

f(1,2,3,4) fonction avec 4 argument
f((1,2,3,4)) un seul argument
'''
def myelt(*iobj):
    malist=[]
    for elt in iobj:
        if elt%2 == 0:
            malist.append(elt)
    return malist

l = [1,2,3,4]
print(myelt(*l))
