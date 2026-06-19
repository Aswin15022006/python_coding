class Solution:
   def checkPerfectNumber(self, num: int) -> bool:
    no = num
    tot = 1  # start from 1 (always a divisor)
    i = 2
    while i * i <= no:
        if no % i == 0:
            tot = tot + i
            if i != no // i:        # avoid counting square root twice
                tot = tot + (no // i)
        i += 1
    if num <= 1:
        return False
    if num == tot:
        return True
    else:
        return False
