calss Solution:
    def getSingle(self,arr,n):
        ans = 0
        for i in range(len(arr)):
            ans ^= arr[i]
        return ans

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        n = int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        ans = ob.getSingle(arr,n)
        print(ans)
        T -= 1
