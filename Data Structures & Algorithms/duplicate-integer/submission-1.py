class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Flag = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] == nums[j]:
                    Flag = True
                    return Flag
        return Flag