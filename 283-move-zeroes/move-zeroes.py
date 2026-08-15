class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # timecomplecity is O(n^2)
        # for i in range(0,len(nums)):
        #     if nums[i]==0:
        #         j=i+1;
        #         while j<len(nums):
        #             if nums[j]!=0:
        #                 nums[i],nums[j]=nums[j],nums[i]
        #                 break;
        #             j+=1; 
            
        # optimal solution
        inser_pos=0;
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[inser_pos],nums[i]=nums[i],nums[inser_pos];
                inser_pos+=1;