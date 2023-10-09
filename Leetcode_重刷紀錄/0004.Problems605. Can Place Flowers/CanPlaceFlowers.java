// 605. Can Place Flowers
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        if(flowerbed[0]==0 && (flowerbed.length< 2||flowerbed[1]==0)){
            flowerbed[0] = 1; 
            count++;
        }
        for (int i = 1; i < flowerbed.length -1 && count < n; ) {
                if (flowerbed[i] +flowerbed[i - 1] + flowerbed[i + 1] == 0) {
                    flowerbed[i] = 1;
                    count++;
                    i+=2;
                }else{
                    i++;
                }
        }
        if(flowerbed[flowerbed.length - 1]==0 && flowerbed[flowerbed.length - 2]==0) count++;
        return count >= n;
    }
}