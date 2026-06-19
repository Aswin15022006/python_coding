class Solution:
    def mirrorDistance(self, n: int) -> int:
        ans=str(n)[::-1]
        ans1=int(ans)
        return abs(n-ans1)
       
