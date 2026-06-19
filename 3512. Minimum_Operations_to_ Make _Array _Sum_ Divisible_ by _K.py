class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        for i in nums:
            ans=ans+i
        tot=ans % k
        return tot    
        
