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

        if(tCount.size() != sCount.size()) {
            return false;
        }

        for (Character key : sCount.keySet()){
            Integer tLetterCount = tCount.get(key);
            Integer sLetterCount = sCount.get(key);

            if(tLetterCount == null || !tLetterCount.equals(sLetterCount) ) {
                return false;
            }
        }

        return true;
    }
}
