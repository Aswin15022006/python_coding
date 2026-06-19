class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=sorted(nums,reverse = True);  
              
        for i in range(k):
            d=l[i];
        return d;    
       
