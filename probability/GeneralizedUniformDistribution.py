#  Modify your code to create probability vectors, p, of arbitrary
#  size, n. Use n=5 to verify that your new solution matches
#  the previous one.

p=[]
n=5

for i in range(0, 5):
    p.append(1.0/n)

print(p)
