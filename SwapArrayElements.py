class Solution:
    def swapElements(self,arr,n):
        for i in range(len(arr)-2):
            arr[i],arr[i+2] = arr[i+2],arr[i]
        return arr
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int,input().split()))
        obj = Solution()
        obj.swapElements(arr,n)
        for i in arr:
            print(i,end = " ")
        print()
