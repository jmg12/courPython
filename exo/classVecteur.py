# /usr/bin/python
# -*- coding: utf-8 -*-
'''
Commencer par la base, pour que l'on puisse écrire
>>> v = V(-3,4)
>>> v
V(-2, 4)

>>> len(v) longueur du vecteur (norme)
2
>>> abs(v) dimension du vecteur (nb de coordonne
5.0

'''

class V(object):
    """ This class implements vectors."""
        
    def __init__(self, *coords):
        """*attr : attribue non défini"""
        self.coords = coords
    
    def __len__(self):
        return len(self.coords)
    
    def __repr__(self):
        
        #return "{}({})".format( param1, param2) equivalent
        return "%s(%s)" % (
            self.__class__.__name__, #nom de la classe
            ', '.join()(repr(c) for c in coords),   
            # la dernier virgule est facultative, au cas où la prochaine ligne on oublie
        '''
        for c in coords:
            ', '.join(repr(c))
        return self(c)
        '''
        )

    def __abs__(self):
        #somme d'un itérable
        return sum(c ** 2 for c in self.coords) ** .5
        '''
        res = 0
        for c in self.coords:
            res += c ** 2 #puissance
        return res ** .5 #racine carré
        '''
    
    def __eq__(self, other):
        return self.coords == other.coords
        
    def __ne__(self, other):
        return not(self == other)

    def __add__(self,other):
        '''
        addition de 2 vecteur
        '''
        #print("__add__ !! self: %r, other: %r" % (self, other))
        if len(self) != len(other):
            raise ValueError('VTFF')
            
        return self.__class__(*(
            a + b for a, b in zip(self.coords, other.coords)
        ))
        
        '''
        self.__class__() = V()
        
        autre moyen
        res = [a + b for a, b in zip(self.coords, other,coords)]
        return self.__class__(*res) #ça fait un tuple
        '''

        
        '''
        méthode 1
        res = []
        for a, b in zip(self.coords, other.coords):
            res.append(a + b)

        '''
        
        '''
        méthode 2
        
        for i, v in enumerate(self.coords):
            res.append(v + other.coords[i])
        '''
         
        '''
        méthode 3
        i = 0
        while i < len(self):
            res.append(self.coords[i] + other.coords[i])
            
        return self.coords + other.coords
        '''
        
    def __rmul__(self,other):
        return self.__class_(*( #appel avc nb arbitraire
            other * c for c in self.coords
        ))

    def __mul__(self, other):
        '''
        multiplication de 2 vecteur
        somme des produits des coords
        '''
        if len(self) != len(other):
            raise ValueError('VTFF')
        return sum(a * b for a, b in zip(self.coords, other.coords))
