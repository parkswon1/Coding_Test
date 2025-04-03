import java.lang.*;

class Solution {
    public String solution(String myString) {
        String answer = myString.toLowerCase();
        StringBuffer str = new StringBuffer(answer);
        for (int i = 0; i < answer.length(); i++) {
            if (str.charAt(i) == 'a') {
                str.setCharAt(i, 'A');
            }
        }
        return str.toString();
    }
}