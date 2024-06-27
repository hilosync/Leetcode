class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        counter = 0

        i = 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                counter += 1
                i += 1

        return counter

        