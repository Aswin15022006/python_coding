class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        sig=1
        for i in str(n):
            s+=int(i)*sig            
            sig=-sig
        return s    


        
