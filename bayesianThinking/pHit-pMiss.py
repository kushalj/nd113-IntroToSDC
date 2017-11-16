#Write code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

for i in range(0, len(p)):
    if i == 1 or i == 2:
        p[i] = p[i]*0.6
    else:
        p[i] = p[i]*0.2


# print(p)

print(sum(p))
