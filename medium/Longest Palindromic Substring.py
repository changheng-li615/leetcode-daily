class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # both left and right got one more step
            # s[a:b] includ a and not includ b, so we dont need to change the position for right
            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            odd = expandFromCenter(i, i)
            even = expandFromCenter(i, i+1)
            curr_longest = odd if len(odd) > len(even) else even
            if len(curr_longest) > len(longest):
                longest = curr_longest

        return longest
