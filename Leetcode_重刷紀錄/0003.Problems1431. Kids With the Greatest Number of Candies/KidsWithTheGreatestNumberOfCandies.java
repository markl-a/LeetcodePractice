//1431. Kids With the Greatest Number of Candies
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
//比較簡潔但是跑得比較慢 耗的記憶體也比較多的方法
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandies = Arrays.stream(candies).max().getAsInt();

        return Arrays.stream(candies)
                     .mapToObj(candy -> candy + extraCandies >= maxCandies)
                     .collect(Collectors.toList());
    }
}

//這個是chatgpt給的解法，跑得比較快記憶體也使用較少
import java.util.List;

public class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandies = 0;
        for (int candy : candies) {
            maxCandies = Math.max(maxCandies, candy);
        }

        List<Boolean> result = new ArrayList<>(candies.length);
        for (int candy : candies) {
            result.add(candy + extraCandies >= maxCandies);
        }

        return result;
    }
}