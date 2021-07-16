#FINDING MINIMUM AND MAXIMUM ELEMENTS OF AN ARRAY

def getMinMax(a, n):
    mi,ma = a[0],a[0]
    for i in a:
        if i < mi:
            mi = i
        elif i > ma:
            ma = i
    return ma,mi

arr = [int(i) for i in input().split()]
n = len(arr)
print(getMinMax(arr,n))
