import java.lang.*;

class Solution {
    public String solution(String n_str) {
        int i = 0;
        
        while (i < n_str.length() && n_str.charAt(i) == '0') {
            i++;
        }

        return n_str.substring(i);
    }
}