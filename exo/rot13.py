# /usr/bin/python

'''
    Fonction qui prend en argument une chaine de caracteres
    et retourne la meme chaine avec les lettres encodees en rot13
    NB: ord() prend un caractere (chaine de longueur un) et renvoie son code ASCII;
    chr() fait l'inverse.
    NB: nous verrons qu'il existe une methode directe pour effectuer 
    cette operation
    
    compare chaine : c < 'a'
    compare nombre : 0 < n < 12
'''
'''
def rot13(chaine):
    res = ""
    for elt in chaine:
        if 'a' <= elt <= 'm' or 'A' <= elt <= 'M':
            res += chr(ord(elt) + 13)
        elif 'n' <= elt <= 'z' or 'N' <= elt <= 'Z':
            res += chr(ord(elt) - 13)
        else:
            res += elt
    return res
'''

def rot13(val):
    res = []
    for elt in val:
        if 'a' <= elt <= 'm' or 'A' <= elt <= 'M':
            res.append(chr(ord(elt) + 13))
        elif 'n' <= elt <= 'z' or 'N' <= elt <= 'Z':
            res.append(chr(ord(elt) - 13))
        else:
            res.append(elt)
    return ''.join(res)

print(rot13("ab"))
