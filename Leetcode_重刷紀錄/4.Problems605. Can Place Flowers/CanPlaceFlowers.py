# 605. Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        if flowerbed[0] == 0 and ( len(flowerbed) <= 1  or flowerbed[1] == 0 ):
            count =1
            flowerbed[0] = 1
        i = 1
        while i < len(flowerbed)-1:
            if flowerbed[i] +flowerbed[i - 1] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:  
                i += 1
        if flowerbed[len(flowerbed)-1] == 0 and  flowerbed[len(flowerbed)-2] == 0 :
            count +=1

        return count >= n   