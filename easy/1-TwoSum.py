#The complexity is O(N)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = {}
        for i , num in enumerate (nums) :
            sub = target - num 
            if sub in L :
                return L[sub] , i
            L[num] = i
            