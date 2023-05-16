grammar = {}
with open('tastatura2.txt', 'r') as file:
    lungime = int(file.readline())
    #print(lungime)
    for line in file:
        line = line.strip()
        if line:
            lhs, rhs = line.split('->')
            lhs = lhs.strip()
            rhs = rhs.strip()
            grammar[lhs] = [s.strip() for s in rhs.split('|')]

# print(grammar)

L = []
l = []

for keys, values in grammar.items():
    for key in keys:
        l.append(key)
        m = grammar[key]

        for nr in m:
            if (len(nr)==2 and nr!='Î»'):
                v = [key, nr[0], nr[1]]
                L.append(v)
            else:
                if(nr=='Î»'):
                    v = [key, 'λ']
                    L.append(v)
                else:
                    v=[key,nr]
                    L.append(v)

#print(L)
cuvant = []
noduri = ['S']


def cuv(indice):
    if indice==lungime:
        nod2=noduri[len(noduri)-1]
        for n in L:
            if n[0]==nod2 and n[1]=='λ':
                result=cuvant
                result=''.join(cuvant)
                print(result)
                if cuvant:
                    cuvant.pop()
                    noduri.pop()
                return 0
        if cuvant:
            cuvant.pop()
            noduri.pop()
        return 0
    else:
        for n in L:
            if n[0] == noduri[indice]:
                if len(n)==3:
                    cuvant.append(n[1])
                    noduri.append(n[2])
                    cuv(indice+1)
                else:
                    if n[1]!='λ' and indice+1==lungime:
                        cuvant.append(n[1])
                        result = cuvant
                        result = ''.join(cuvant)
                        print(result)
                        cuvant.pop()
                        return 0
        if cuvant:
            cuvant.pop()
            noduri.pop()
        return 0


cuv(0)