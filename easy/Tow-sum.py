class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        "hashmap to store value with key"
        hashmap={}
        
        "according to enumerate function -> generate index and value"
        "i=key and num=value"
        for i,num in enumerate(nums):

            "our target value - the number e.g. 9 - 7 = 2 now we can find 2 in our hashmap"
            if target - num in hashmap:
                "if correct"
                "return two index numbers 7 and 2"
                return [i,hashmap[target-num]]
            "if cant find, give the value into hash map with index i"
            hashmap[num] = i