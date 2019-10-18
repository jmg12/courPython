# /usr/bin/python

'''
Ecrire un generateur qui prend en argument une fonction f 
et une valeur x et genere x,f(x),f(f(x)), etc.
'''

def gen_values(f,x):
    while True:
        yield x
        x = f(x)
        #yield f(x)
        #yield f(f(x))
    #yield f

'''
def gen_values(f, x):
    yield x
    #yield from gen_values(f, f(x))
    for val in gen_values(f, f(x)):
        yield val
# yield from x
'''

for i in gen_values(lambda x: x + 1, 0):
    print(i)
    if i>=10:
        break

#set(gen_values())
'''
for i in gen_values(lambda x: x + "a", ""):
    print(i)
    if len(i) >= 10:
        break
'''

'''
def f_inc(x):
    return x + 1

for i in gen_values(f_inc,0)
    print(i)
    if i>=10:
        break
'''
