class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans=[]
        k=len(nums)
        for i in range(k):
            if(nums[i]%2==0):                
                ans.append(0)
            else:
                ans.append(1)
        return sorted(ans)
