#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(0, len(p)):
        hit = (Z == world[i])
        q.append( p[i] * (pHit*hit + pMiss*(1-hit)) )

    total_pr = sum(q)

    for i in range(len(q)):
        q[i] = q[i] / total_pr

    return q

print(sense(p,Z))
