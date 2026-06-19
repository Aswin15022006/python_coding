class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot=sum(nums)
        s=0
        h=nums
        for i in h:
            for j in str(i):
                 s+=int(j)
        return tot-s    
        

        
