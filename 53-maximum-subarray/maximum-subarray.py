class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force O(n^2)
        # max_arr=float('-inf');
        # for i in range(0,len(nums)):
        #     addition=0;
        #     for j in range(i,len(nums)):
        #         addition=addition+nums[j];
        #         max_arr=max(max_arr,addition);
        # return max_arr;


        # Optimal Solution 
        # O(n)

        max_subArray=nums[0];
        max_addition=nums[0];
        for i in range(1,len(nums)):
            max_addition=max(nums[i],max_addition+nums[i]);
            max_subArray=max(max_addition,max_subArray);

        return max_subArray;