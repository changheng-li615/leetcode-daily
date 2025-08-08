class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        "time complexcity for search in Set Type is O(1)"
        "in List type is O(n) so we change to Set type" 
        num_set = set(nums)


        for n in num_set:
            
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest