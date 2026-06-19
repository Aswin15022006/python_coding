class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tot=0
        rem=1
        div=0
        while(n!=0):
            tot=n%10
            rem=tot*rem
            div=tot+div
            ans=rem-div
            n=n//10
        return ans    


        
