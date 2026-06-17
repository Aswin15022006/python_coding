class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        return int(n.replace("6","9",1))
        
