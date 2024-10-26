import java.lang.*;

class Solution {
    public String solution(String my_string, String alp) {
        StringBuffer str = new StringBuffer(my_string);
        char targetChar = alp.charAt(0);
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == targetChar){
                str.setCharAt(i, Character.toUpperCase(targetChar));
            }
        }
        return str.toString();
    }
}