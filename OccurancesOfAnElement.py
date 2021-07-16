def count(arr, n, x):
    cnt = 0
    for i in arr:
        if i == x:
            cnt += 1
    return cnt

l = [int(i) for i in input().split()]
n = len(l)
ele = int(input())
print(count(l,n,ele))
