'''
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side.
The rightmost element is always a leader. 

 

Example 1:

Input:
-------
n = 6
A[] = {16,17,4,3,5,2}

Output: 17 5 2

Explanation:
------------
The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
 

Example 2:

Input:
------
n = 5
A[] = {1,2,3,4,0}

Output: 4 0
 

Your Task:
----------
You don't need to read input or print anything. The task is to complete the function leader()
which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

 

Constraints:
1 <= n <= 107
0 <= Ai <= 107

'''

class Solution:
    def leaders(self,A,N):
        l = []
        m = A[N-1]
        l.append(m)
        for i in range(N-2, -1, -1):
            if A[i] >= m:
                m = A[i]
                l.append(A[i])
        return l[::-1]

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        N = int(input())
        A = [int(x) for x in input().split()]
        ob = Solution()
        A = ob.leaders(A,N)
        for i in A:
            print(i, end = " ")
        print()
        T -= 1
