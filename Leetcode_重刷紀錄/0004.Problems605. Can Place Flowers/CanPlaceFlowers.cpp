// 605. Can Place Flowers
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {      
        if(n ==0)return true;
        int flowerbedSize = flowerbed.size();
        if(!flowerbed[0] && (flowerbedSize< 2||!flowerbed[1]))flowerbed[0] = 1, n--;

        for (int i = 1; i < flowerbedSize-1; i += (flowerbed[i] ? 2 :1)) {
            if (!(flowerbed[i] || flowerbed[i - 1] || flowerbed[i + 1])) 
            flowerbed[i] = 1, n--;
        }
        if(!(flowerbed[flowerbedSize - 1]|| flowerbed[flowerbedSize - 2])) n--;

        return n <= 0;
    }
};