class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        count=0

        for i in nums:
            if target - i in m:
                return [m[target-i], count]
            m[i] = count
            count = count + 1

        return []