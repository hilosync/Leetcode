class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        def recursive(left,right):
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid

            if mid == left or mid == right:
                return -1

            if nums[mid] < target:
                return recursive(mid, right)
            
            else:
                return recursive(left, mid)

        return recursive(0, len(nums))
