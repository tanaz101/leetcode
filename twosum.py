class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            if index!=len(nums)-1: 
                for next_index in range(index+1,len(nums)):
                    sum= nums[index]+nums[next_index]
                    if sum==target:
                        return[index,next_index]
                        break
