class Solution {
    public int[] twoSum(int[] nums, int target) {
        // we can use the complement approach
        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            Integer seenBeforeIndex = seen.get(complement);
            if (seenBeforeIndex != null) {
                return new int[]{seenBeforeIndex, i};
            }
            seen.put(nums[i], i);
            
        }
        return new int[]{0, 1};
    }
}
