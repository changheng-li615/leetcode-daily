class Solution:
    def countSubstrings(self, s: str) -> int:
         def expandFromCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

         total = 0
         for i in range(len(s)):
            total += expandFromCenter(i, i)
            total += expandFromCenter(i, i + 1)

         return total
        