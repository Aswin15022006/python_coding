class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans1=celsius+273.15
        ans2=celsius*1.80+32.00
        tot1=float(ans1)
        tot2=float(ans2)
        
        return [tot1,tot2]

        
