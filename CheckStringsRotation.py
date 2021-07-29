'''
CHECK IF STRING IS ROTATED BY TWO PLACES
-------------------------------------------
Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

Example 1:
------------
Input:
-------
a = amazon
b = azonam

Output:
-------
1

Explanation:

amazon can be rotated anti
clockwise by two places, which will make
it as azonam.

Example 2:
-----------
Input:
------
a = geeksforgeeks
b = geeksgeeksfor

Output:
-------
0

Explanation: If we rotate geeksforgeeks by
two place in any direction , we won't get
geeksgeeksfor.

Your Task:
------------
The task is to complete the function isRotated() which takes two strings as input parameters and checks if given strings can be formed by rotations. The function returns true if string 1 can be obtained by rotating string 2 by two places, else it returns false.

Expected Time Complexity: O(N).
Expected Auxilary Complexity: O(N).
Challenge: Try doing it in O(1) space complexity.

Constraints:
1 <= length of a, b < 100

'''
def rightrotate(str1,str2):
    s,n,k = '',len(str1),2
    for i in range(n):
        if i < k:
            s += str1[n+i-k]
        else:
            s += str1[i-k]
    return s
def leftrotate(str1,str2):
    s,n,k = '',len(str1),2
    for i in range(n):
        s += str1[(k+i)%n]
    return s
class Solution:
    def isRotated(self,str1,str2):
        if rightrotate(str1,str2) == str1:
            return 1
        elif leftrotate(str1,str2) == str2:
            return 1
        else:
            return 0
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        p = input()
        if Solution().isRotated(s,p):
            print(1)
        else:
            print(0)
