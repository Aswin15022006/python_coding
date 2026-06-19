
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sig=1
        tot=0
        for i in nums:
            tot+=i*sig
            sig=-sig
        return tot  
