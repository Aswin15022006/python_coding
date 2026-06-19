class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans=str(n)
        d0=int(ans.count("0"))*0
        d1=int(ans.count("1"))*1
        d2=int(ans.count("2"))*2
        d3=int(ans.count("3"))*3
        d4=int(ans.count("4"))*4
        d5=int(ans.count("5"))*5
        d6=int(ans.count("6"))*6
        d7=int(ans.count("7"))*7
        d8=int(ans.count("8"))*8
        d9=int(ans.count("9"))*9
        return d0+d1+d2+d3+d4+d5+d6+d7+d8+d9

        
        

        

        
        
        
