v=4
adj=[[1,2,3],[0],[0],[0]]


r=[-1,-1,-1,-1]
r[0]=0
a=[False,False,False,False]
for u in range(1,v):
    for i in adj[u]:
        if(r[i]!=-1):
            a[r[i]]=True
    cr=0
    while(cr<v):
        if(a[cr]==False):
            break
        cr+=1
    r[u]=cr
    for i in adj[u]:
        if(r[i]!=-1):
            a[r[i]]=False
for i in range(v):
    print("vertex ",i," color ",r[i])
    

