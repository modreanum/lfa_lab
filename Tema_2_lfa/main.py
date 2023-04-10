f = open("tastatura4.txt", "r")
stinit = f.readline()
stinit = int(stinit[1:])

linie1 = f.readline()
L = []
linie1 = [x for x in linie1.split()]

for linie in f.readlines():
    linie = [x for x in linie.split()]
    linie1[0] = int(linie1[0][1:])
    linie1[2] = int(linie1[2][1:])
    L.append(linie1)
    linie1 = linie

fin = linie
for x in range(0, len(fin)):
    fin[x] = int(fin[x][1:])

maxim = 0
for l in L:
    if l[0] > maxim:
        maxim = l[0]
    if l[0] > maxim:
        maxim = l[0]

alfabet = []
for x in L:
    if x[1] not in alfabet:
        alfabet.append(x[1])

M = []
for i in range(1, maxim+1):
    m = [0] * i
    M.append(m)

for x in fin:
    for i in range(0, x):
        M[x - 1][i ] = "λ"

import itertools
liste=[]
for i in range(1,maxim+1):
    lista=[p for p in itertools.product(alfabet, repeat=i)]
    liste.extend(lista)
noduri=[]
for x in range(0,maxim):
    if x not in fin:
        noduri.append(x)
for inp in liste:
    acceptat=[]
    neacceptat=[]
    for nod in noduri:
        drum = []
        ok = 1
        p1 =nod
        drum.append(p1)
        y = 0
        ok = 1
        while y < len(inp) and ok:
            ok = 0
            for x in L:
                if x[0] == p1 and y < len(inp) and x[1] == inp[y]:
                    p1 = x[2]
                    drum.append(p1)
                    y = y + 1
                    ok = 1

        if drum[len(drum) - 1] not in fin:
            ok = 0
        if ok == 0 or y != len(inp):
            neacceptat.append(nod)
        else:
            acceptat.append(nod)

    if len(acceptat)>0 and len(neacceptat)>0:
        for a in acceptat:
            for b in neacceptat:
                if a>b:
                    if(M[a-1][b]==0):
                        M[a-1][b]=inp
                else:
                    if (M[b - 1][a] == 0):
                        M[b-1][a] = inp

for i in range(0,maxim):
    for j in range(0,i+1):
        if M[i][j]==0:
            a=i+1
            if j==0:
                b=str(j)+str(a)
            else:
                if a < j:
                    b=a*10+j
                else:
                    b=j*10+a
            if stinit==a or stinit==j:
                stinit=b
            for z in range(0,len(fin)):
                if fin[z]==a or fin[z]==j:
                    fin[i]=b
            for l in L:
                if l[0]==a or l[0]==j:
                    l[0]=b
                if l[2] == j or l[2]==a:
                    l[2] =b

newL=[]
for l in L:
    if l not in newL:
        newL.append(l)

stinit=str(stinit)
stinit="q"+stinit
for i in range(len(fin)):
    fin[i]="q"+str(fin[i])
for l in L:
    l[0]="q"+str(l[0])
    l[2]="q"+str(l[2])

import sys
with open('output.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('stare initiala',stinit)
    print("stari finale:")
    for x in fin:
        print(x)
    print()
    for l in newL:
        print(l[0],l[1],l[2])


f.close()