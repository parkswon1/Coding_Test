import java.lang.*;

class Solution {
    public int solution(String myString, String pat) {
        StringBuffer str = new StringBuffer(myString);
        for(int i = 0; i < str.length(); i++){
            if (str.charAt(i) == 'A'){
                str.setCharAt(i,'B');
            } else {
                str.setCharAt(i,'A');
            }
        }
        if (str.toString().contains(pat)){
            return 1;
        }
        return 0;
    }
}