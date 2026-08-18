class Solution {
    public int maxArea(int[] heights) {
        int maximun = 0;
        int l = 0;
        int r = heights.length - 1;
        // to calculate the height lets start why iterating
        while(l < r ) {
            int distance = r - l;
            int area = distance * Math.min(heights[r], heights[l]);
            maximun = Math.max(area,maximun);
            // lets move the lower bar;
            if(heights[l] < heights[r]) {
                l++;
            }else {
                r--;
            }
        }
        return maximun;
    }
}
