"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=50000 # sqrt(2 power of 31) --> 46340... 
        mid=(left+right)//2
        while(True):
            temp=mid
            if mid*mid>x:
                right=mid+1
            else:
                left=mid
            mid=(left+right)//2
            if temp==mid:
                break
        return left
