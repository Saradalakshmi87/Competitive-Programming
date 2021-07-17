class Solution:
    def rearrange(self,arr,n):
        self.l = []
        while len(arr):
            self.l.append(max(arr))
            arr.remove(max(arr))
            if len(arr):
                self.l.append(min(arr))
                arr.remove(min(arr))
        return self.l
if __name__ == '__main__':
    T = int(input())
    while T>0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        res = ob.rearrange(arr,n)
        for i in res:
            print(i,end = " ")
        print()
        T -= 1
'''
    OTHER APPRAOCH
-----------------------

    s,e = 0,n-1
    l = []
    while s<=e:
        l.append(arr[e])
        e -= 1
        l.append(arr[s])
        s += 1
    for i in range(n):
        arr[i] = l[i]
    return arr
    
'''
