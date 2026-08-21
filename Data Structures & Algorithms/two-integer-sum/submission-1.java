class Solution {
    public int[] twoSum(int[] nums, int target) {
        // we can use the complement approach
        HashMap<Integer, Integer> complements = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            Integer seenBeforeIndex = complements.get(complement);
            if (seenBeforeIndex != null) {
                return new int[]{seenBeforeIndex, i};
            }
            complements.put(nums[i], i);
            
        }
        return new int[]{0, 1};
    }
}
