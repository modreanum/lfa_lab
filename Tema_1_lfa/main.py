f = open("tastatura1.txt", "r")
inp=input("input=")
#stinit=input("stare initiala=")
#stinit=int(stinit[1:])
lenght=len(inp)
linie1=f.readline()
L=[]
linie1 = [x for x in linie1.split()]
for linie in f.readlines():
    linie = [x for x in linie.split()]
    linie1[0]=int(linie1[0][1:])
    linie1[2] =int(linie1[2][1:])
    L.append(linie1)
    linie1=linie
#print(L)
fin=linie
for x in range(0,len(fin)):
    fin[x]=int(fin[x][1:])
#print(fin)
drum=[]
ok=1
#p1=stinit
p1=0
drum.append(p1)
y=0
ok=1
while y<len(inp) and ok:
    ok=0
    for x in L:
        if x[0]==p1 and y<len(inp) and x[1]==inp[y] :
            p1=x[2]
            drum.append(p1)
            y=y+1
            ok=1

if drum[len(drum)-1] not in fin:
    ok=0
if ok==0 or y!=len(inp):
    print("neacceptat")
else:
    print("acceptat")
    print(drum)
f.close()
