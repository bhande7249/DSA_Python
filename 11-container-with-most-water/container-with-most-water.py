class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length=len(height)-1;
        maxArea=float('-inf');
        i=0;
        j=len(height)-1;
        while i <j:
            area=min(height[i],height[j])*length;
            # print(area);
            maxArea=max(maxArea,area);
            if height[i]<height[j]:
                i+=1;
                length-=1;
            else:
                j-=1;
                length-=1;
        return maxArea;  
        