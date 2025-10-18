class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        ans=[]
        while left < right:
            if numbers[left]+numbers[right]==target:
                ans.extend([left+1,right+1])
                break
            elif numbers[left]+numbers[right]< target:
                left+=1
            else:
                right-=1
        return ans
        