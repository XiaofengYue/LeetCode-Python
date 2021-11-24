class Solution:
    def getMaxLen(self, nums):
        n = len(nums)
        positive = [0]*n
        negative = [0]*n
        
        if nums[0]>0:
            positive[0]=1
        elif nums[0]<0:
            negative[0]=1
        maxlength = positive[0]
        for i in range(1,n):
            if nums[i]>0:
                positive[i] = positive[i-1]+1
                negative[i] = (negative[i-1]+1 if negative[i-1]>0 else 0)
            elif nums[i]<0:
                positive[i] = (negative[i-1]+1 if negative[i-1]>0 else 0)
                negative[i] = positive[i-1]+1
            else:
                positive[i] = negative[i]=0
            maxlength = max(maxlength,positive[i])
        return maxlength