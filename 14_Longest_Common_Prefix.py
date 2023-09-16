"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):  
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res

# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# * unpack the str
