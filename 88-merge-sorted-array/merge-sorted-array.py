class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # if m==1:
        #     return;
        # elif n==1:
        #     nums1[0]=nums2[0];
        #     return;
        # j=m-1
        # for i in range(0,len(nums1)):
        # # for num in nums1:
        #     # if nums1[i]==0:
        #         nums1[j]=nums2[j]
        #         j+=1;
        # nums1.sort();

        i=m;
        for num in nums2:
            nums1[i]=num;
            i+=1;
        nums1.sort();