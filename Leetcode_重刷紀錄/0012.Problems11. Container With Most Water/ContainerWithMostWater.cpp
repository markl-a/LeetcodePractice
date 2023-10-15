//11. Container With Most Water
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxArea = 0,w;

        while ((w = right - left)) {
            if (height[left] < height[right]) {
                    maxArea = max(maxArea, height[left++] * w);   
                    } else {
                    maxArea = max(maxArea, height[right--] * w); 
                    }           
        }
        return maxArea;
    }
};