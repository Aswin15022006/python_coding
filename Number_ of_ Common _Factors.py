class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        while b != 0:
             a, b = b, a % b
        count=1
        for i in range(1,a):
            if((a%i==0)and(b%i==0)):
                  count=count+1
        return count        

        
        
        
