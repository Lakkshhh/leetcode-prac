class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_pointer = 1

        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer - 1]:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
        
        return slow_pointer