# /usr/bin/python

'''
fabriquer un generateur
'''

def gen_words(fname):
    with open(fname) as fdesc:
        for line in fdesc:
            for word in line.split():
                yield word

for word in gen_words("toto.txt"):
    print(word)

#contructeur set genere un ensemble unique qui n'a pas d'ordre
set(gen_words("toto.txt"))
'''
#la liste des mots dans l'ordre apparue
list(gen_words("toto.txt"))
'''
