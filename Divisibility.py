n = int(input())
l = [int(i) for i in input().split()][:n]
if l[-1]%10 == 0:
    print("Yes")
else:
    print("No")
