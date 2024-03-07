from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            if target - nums[i] in nums:
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i
        return []
    