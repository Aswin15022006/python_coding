class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tot=0
        ans=0
        for i in range(1,n+1):
            if(i%m!=0):
                tot=tot+i
            else:
                ans=ans+i
        return tot-ans            
        
