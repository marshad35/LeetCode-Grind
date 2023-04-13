class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums.sort()
        start = -2
        if(len(nums)==0):
            return 0
        for i in range(len(nums)):
            if(nums[i] == val):
                start = i
                break
        if(start == -2):
            return len(nums)
        while len(nums)-1 >= start:
            if(nums[start] != val):
                break
            nums.pop(start)
        return len(nums)
            