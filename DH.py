
# P Prime 
# G primitive root of P
# PUBLIC KEYS : P , G



PRlist=[]
def checkifPR(n,p):
    index=1
    table=[]
    while index<p:
        x=pow(n,index,p)
        if x in table:
            return "notPR"
        else:
            table.append(x)
        
        index+=1
    PRlist.append(n)
    return "YesPR"
print("Enter a Prime Number")
P=int(input())
for i in range(P):
    checkifPR(i,P)
j=0
print("Primary Root List")
for PR in PRlist:
    print(f'Press: {j} for {PR}')
    j+=1
print("\nChoose a Primary Root as (Integer)")
Y=int(input())
G=PRlist[Y]


print(f'\nPublically known \nPrime no: {P}\nPrimitive Root: {G}')

#Alice
print("Enter Alice Private Key  (Integer)")
a=int(input())
AE=pow(G,a,P)


#bob
print("Enter Bob Private Key (Integer)")
b=int(input())
BE=pow(G,b,P)

print(f'\nPrivately known \nAlice secret key: {a}\nBob secret key: {b}')
print(f'\nAlice Sent key: {AE}\n Bob Sent key: {BE}')
#exchange


#alice
ADE=pow(BE,a,P)

#bob
BDE=pow(AE,b,P)


print(f'\nAlice final key: {ADE}\n Bob final key: {BDE}')