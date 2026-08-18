class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> sCount = new HashMap<>();
        HashMap<Character, Integer> tCount = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character letter = s.charAt(i);
            sCount.merge(letter, 1, Integer::sum);
        }

       for (int i = 0; i < s.length(); i++) {
            Character letter = t.charAt(i);
            tCount.merge(letter, 1, Integer::sum);
        }

        return sCount.equals(tCount);
    }
}
