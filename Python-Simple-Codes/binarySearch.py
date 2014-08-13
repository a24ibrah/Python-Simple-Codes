
# Binary search algorithm
def binary_search(data, target, low, high, noOfSteps):
    noOfSteps +=1
    if low > high:
        return False # interval is empty; no match
    else:  
        mid = (low + high) // 2
        if target == data[mid]:
            return (True,noOfSteps,mid)
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1, noOfSteps)
        else:
            return binary_search(data, target, mid+1, high, noOfSteps)

"""import random        
for i in range(0, 10):
    data.append(random.randint(1,10))"""
data = range(0,10)
noOfSteps = 0
d = binary_search(data,6,0,9, 0)
print ("The result of binary search is {}, in {} step(s), location of target is in data[{}]".format(d[0],d[1],d[2]))
 
