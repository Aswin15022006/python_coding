class Solution:
    def addBinary(self, a: str, b: str) -> str:
        g=bin(int(a,2)+int(b,2))
        n=g[2:]
        return n
        

        
