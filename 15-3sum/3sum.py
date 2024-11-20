class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []

        for index, number in enumerate(nums):
            if number > 0:
                break
            
            if index != 0 and number == nums[index-1]:
                continue
            
            leftPointer = index+1
            rightPointer = len(nums)-1
            
            while leftPointer < rightPointer:
                currSum = number + nums[leftPointer] + nums[rightPointer]

                if currSum == 0:
                    results.append([number, nums[leftPointer], nums[rightPointer]])
                    rightPointer -= 1
                    leftPointer += 1

                    while nums[leftPointer] == nums[leftPointer-1] and leftPointer < rightPointer:
                        leftPointer += 1
                
                elif currSum > 0:
                    rightPointer -= 1
                
                else:
                    leftPointer += 1
            
        return results