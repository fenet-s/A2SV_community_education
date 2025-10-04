class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         sorted_nums=sorted(nums)
         result=[]
         for i in range(len(nums)):
            target=nums[i]
            result.append(sorted_nums.index(target))
         return result
         #sorted=[1,2,2,3,8] i=3 target=2 result=[4,0,2,2,3]
       

         
        