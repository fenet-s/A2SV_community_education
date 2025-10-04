class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:  
        result=[]
        sorted_nums = sorted(nums)
        for num in range(len(nums)):
            if sorted_nums[num]==target:
                result.append(num)
        return result
                

        