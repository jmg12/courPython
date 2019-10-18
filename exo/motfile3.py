# /usr/bin/python

'''
    Ecrire une fonction qui prend en argument le nom d'un fichier et donne 
    en sortie les mots (uniques) utilises.
    Pour simplifier, on considere que le fichier contient seulement des 'mots' et
    des espaces (" ", "\t", "\n")
    
'''

def mfile(nomfile):
  
#Python 2  
    with open(nomfile) as fdesc:
        return {mot for ligne in fdesc for mot in ligne.split()}
    '''
        mots = set(mot for ligne in fdesc for mot in ligne.split())
    return mots
    '''

'''
#python 3
    with open(nomfile) as fdesc:
        return {
            mot
            for line in fdesc
            for mot in line.split()
        }
'''
print(mfile("toto.txt"))

