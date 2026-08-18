class Solution {
    public int removeDuplicates(int[] nums) {
        int length = nums.length, l = 1, r = 1;
        for (r = 1; r<length; r++) {
            if(nums[r] != nums[r-1]) {
                nums[l] = nums[r];
                l++;
            }
        }
        return l;
    }
}