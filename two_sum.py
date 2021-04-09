from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in nums and idx != nums.index(complement):
                return [idx, nums.index(complement)]


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15,23,45,12,3,6], 26))