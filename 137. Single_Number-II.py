class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t1=0
        t2=0
        for num in nums:
            t1^=(num & (~t2))
            t2^=(num & (~t1))
        return t1    

        
