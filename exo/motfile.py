# /usr/bin/python

'''
    Ecrire une fonction qui prend en argument le nom d'un fichier et donne 
    en sortie les mots (uniques) utilises.
    Pour simplifier, on considere que le fichier contient seulement des 'mots' et
    des espaces (" ", "\t", "\n")
    
'''

'''
def mfile(nomfile):
    #Ensemble set()
    mots = set()
    for ligne in open(nomfile):
        for mot in ligne.split():
            if mot not in mots:
                mots.add(mot)
    return mots
'''    
#script ameliore
def mfile(nomfile):
    #Ensemble set()
    mots = set()
    for ligne in open(nomfile):
        mots.update(ligne.split())
    return mots
        
print(mfile("test.txt"))
