class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))!=len(nums)
        dic={}
        count=0
        for i in nums:
            if i in dic:
                dic[i]+=1
                count+=1
            else:
                dic[i]=1
        if count>0:
            return True
        return False

               


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna