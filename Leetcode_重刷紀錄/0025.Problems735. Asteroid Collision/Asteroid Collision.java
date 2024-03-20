class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
       
        for (int ast : asteroids) {
            collision: {
                while (!stack.isEmpty() && ast < 0 && stack.peek() > 0) {
                    if (stack.peek() < -ast) {
                        stack.pop();
                        continue;
                    } else if (stack.peek() == -ast) {
                        stack.pop();
                    }
                    // 如果碰撞發生，且棧頂小行星被摧毀或兩者大小相同，則不將目前小行星加入堆疊
                    break collision;
                }
                // 如果沒有發生碰撞，或堆疊為空，或棧頂小行星向左移動，則將目前小行星加入堆疊
                stack.push(ast);
            }
        }

        // 將堆疊中的元素轉換為數組
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }
}