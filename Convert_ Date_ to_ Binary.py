class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        d = date.split("-")
        binary_parts = [bin(int(part))[2:] for part in d]
        return "-".join(binary_parts)
