class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        if(n < 1 or n > 100000):
            raise ValueError(f"Error: expected 'nums' to have 1 <= size <= 100000 but got {len(nums)}")
        
        hm = set(nums)
        
        if(len(hm) < len(nums)):
            return True
        else:
            return False
        
        

