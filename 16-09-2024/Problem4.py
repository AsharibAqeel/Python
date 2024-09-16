class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord("A"))
            columnNumber //= 26
        return ans[::-1]

sol = Solution()
column_number = 28
result = sol.convertToTitle(column_number)
print(f"Excel column title for {column_number} is: {result}")
