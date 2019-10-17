# /usr/bin/python

'''
    Ecrire une fonction qui prend en argument le nom d'un fichier et donne 
    en sortie les mots utilises ainsi que leur nombre d'occurrences.
    Pour simplifier, on considere que le fichier contient seulement des 'mots' et
    des espaces (" ", "\t", "\n")
    
'''
'''
def cmfile(nomfile):
    #cree un dictionnaire
    mots = {}
    
    for ligne in open(nomfile):
        for mot in ligne.split():
            if mot not in mots:
                mots[mot] += 1
            else:
                mots[mots] = 1

    return mots
    
'''
def cmfile(nomfile):
    #cree un dictionnaire
    mots = {}
    
    for ligne in open(nomfile):
        for mot in ligne.split():
            mots[mot] = mots.get(mot, 0) + 1
    return mots
        
print(cmfile("test.txt"))
