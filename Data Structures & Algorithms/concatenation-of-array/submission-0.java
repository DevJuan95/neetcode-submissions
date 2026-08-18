class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length;
        int[] ans = new int[length*2];
        int j = length;

        for(int i=0; i<length;i++){
            ans[i] = nums[i];
            ans[j] = nums[i];
            j++;
        }
        return ans;
    }
}