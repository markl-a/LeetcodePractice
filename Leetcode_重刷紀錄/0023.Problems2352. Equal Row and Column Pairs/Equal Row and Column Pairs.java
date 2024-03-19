//別人的程式碼
class Solution {
    public int equalPairs(int[][] grid) {
        Map<List<Integer> , Integer> data = new HashMap<>();
        int ans = 0;

        //storing the row elements
        for(int i=0;i<grid.length;i++){
            List<Integer> temp = new ArrayList<>();
            for(int j=0;j<grid.length;j++){
                temp.add(grid[i][j]);
            }
            data.put(temp, data.getOrDefault(temp, 0)+1);
        }

       
        //storing the col elements
        for(int j=0;j<grid.length;j++){
            List<Integer> col = new ArrayList<>();
            for(int i=0;i<grid.length;i++){
                col.add(grid[i][j]);
            }
          
            if(data.containsKey(col)){
                ans+=data.get(col);
            }
        }
        return ans;
    }
}
