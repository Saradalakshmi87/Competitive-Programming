T = int(input())
while T:
    T -= 1
    res1,res2 = 0,0
    cost_of_Gb,cost_of_Pb = map(int,input().split())
    n = int(input())
    for k in range(n):
        i,j = map(int,input().split())
        res1 += (i*cost_of_Gb + j*cost_of_Pb)
        res2 += (j*cost_of_Gb + i*cost_of_Pb)
    print(min(res1,res2))
