class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> seenCounter = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            seenCounter.merge(nums[i], 1, Integer::sum);
            Integer count = seenCounter.getOrDefault(nums[i], 0);
            if(count > 1){
                return true;
            }
        }
        return false;
    }
}