"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums[:] = [i for i in nums if i != val]
        
        

        return len(nums)


"""
* nums[:]. This means that it modifies the original nums list in-place, removing all occurrences of val.

* nums = [i for i in nums if i != val]:
This line also uses list comprehension to create a new list containing all elements from nums that are not equal to val. 
However, it assigns this new list to the variable nums, effectively creating a new list and reassigning it to the same variable name. 
The original nums list remains unchanged, and the variable nums now references the new list without the occurrences of val.
"""
