class Solution {
    public int solution(String myString, String pat) {
        String mainStr = myString.toLowerCase();
        String patStr = pat.toLowerCase();
        if (mainStr.contains(patStr)){
            return 1;
        }
        return 0;
    }
}