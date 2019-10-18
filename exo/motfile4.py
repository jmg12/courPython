# /usr/bin/python
from collections import defaultdict, Counter
'''
    Ecrire une fonction qui prend en argument le nom d'un fichier et donne 
    en sortie les mots utilises ainsi que leur nombre d'occurrences.
    Pour simplifier, on considere que le fichier contient seulement des 'mots' et
    des espaces (" ", "\t", "\n")
    
'''
# (e ? a : b) = (a if e else b)
#help(defaultdict)
    
def cmfile(fname):
    res = defaultdict(int)
        
    with open(fname) as fdesc:
        c = Counter(fname)
        # return {... } equivalent return set()
        return Counter(
            word
            for line in fdesc
            for word in line.split()
        )

print(cmfile("toto.txt"))
