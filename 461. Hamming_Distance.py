class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=x^y;
        d=bin(c)[2:];
        o=d.count("1")
        return o;
        
