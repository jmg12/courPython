# /usr/bin/python

'''meme ennonce que tabpair.py, 
sauf qu'il prend param indefini d'entier avec *
'''
def myelt(*iobj):
    malist=[]
    for elt in iobj:
        if elt%2 == 0:
            malist.append(elt)
    return malist

print(myelt(0,1,2,3))
