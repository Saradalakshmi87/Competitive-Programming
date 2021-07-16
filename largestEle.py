#FINDING THE LARGEST ELEMENT OF ARRAY

def largest(arr, n):
    m = arr[0]
    for i in arr:
        if i > m:
            m = i
    return m

l = [int(i) for i in input().split()]
n = len(l)
print(largest(l,n))
