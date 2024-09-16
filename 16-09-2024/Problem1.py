class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_value = start ^ goal
             
        return bin(xor_value).count('1')
sol = Solution()
start = 20
goal = 10  
print(f"Minimum bit flips to convert {start} to {goal}: {sol.minBitFlips(start, goal)}")
