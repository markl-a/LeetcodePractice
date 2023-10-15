//11. Container With Most Water
public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0,w;
        while ((w = right - left)>0) {
            if (height[left] < height[right]) {
            maxArea = Math.max(maxArea, height[left++] * w);   
            } else {
            maxArea = Math.max(maxArea, height[right--] * w);  
            }
        }
        return maxArea;
    }
}

