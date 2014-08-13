# program to compute sum(x) of n
n = 10
result = 0
for x in range(0, n):
    result += x
print result

#Program to compute sum(ax) of n to the power using Horner's rule
import random
n = 10
a = [ ]
for x in range(0, n):
    a.append(random.randrange(0, 10))
result = len(a);
for x in range(0, n):
    result = result * x + a[x];
    print result
#print result