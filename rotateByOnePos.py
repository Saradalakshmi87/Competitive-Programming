def rotate( arr, n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

l = [int(i) for i in input().split()]
print(rotate(l,len(l)))
