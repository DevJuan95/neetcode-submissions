class Solution {
    public int removeDuplicates(int[] nums) {
        int length = nums.length, l = 1, r = 1;
        while(r<length){
            if(nums[r] == nums[r-1]){
                r++;
            }else {
                nums[l] = nums[r];
                r++;
                l++;
            }
        }
        return l;
    }
}