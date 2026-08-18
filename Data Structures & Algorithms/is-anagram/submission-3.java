class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> string1Counter = new HashMap<>();
        HashMap<Character, Integer> string2Counter = new HashMap<>();
        if( s.length() != t.length() ){
            return false;
        }
        for(char c : s.toCharArray()){
            string1Counter.merge(c, 1, Integer::sum);
        }

        for(char c : t.toCharArray()) {
            string2Counter.merge(c,1, Integer::sum);
        }

        for(char c : s.toCharArray()) {
            Integer countS = string1Counter.get(c);
            Integer countT = string2Counter.get(c);
            if(!countS.equals(countT)) {
                return false;
            }
        }
        return true;
    }
}
