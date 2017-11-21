#For this problem, you aren't writing any code.
#Instead, please just change the last argument
#in f() to maximize the output.

from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

def mu_update(mu, sigma2, nu, r2):
    return (1/(sigma2+r2)) * (r2*mu + sigma2*nu)

def sigma2_update(sigma2, r2):
    return 1 / (1/sigma2 + 1/r2)

# print( f(10.,4.,10.) ) #Change the 8. to something else!
print(mu_update(10., 8., 13., 2.))
print(sigma2_update(8., 2.))
