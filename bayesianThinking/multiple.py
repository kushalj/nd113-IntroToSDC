#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both
#measurements are incorporated. Make sure that your code
#allows for any sequence of measurement of any length.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
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

for m in measurements:
    p = sense(p,m)

print(p)
