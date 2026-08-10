class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0;
        i=0;
        for i in range(i,len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[j]=nums[i];
                j+=1;
        nums[j]=nums[-1];
        return j+1;