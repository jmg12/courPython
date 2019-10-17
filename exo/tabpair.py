# /usr/bin/python
#fonction

''' Fonction prend en argument un objet iterable 
et retourne une liste des elements pairs
NB: utilise module "%"
'''
def myelt(iobj):
    malist=[]
    for elt in iobj:
        if elt%2 == 0:
            malist.append(elt)
    return malist

print(myelt([1,5,2]))
