import java.lang.*;

class Solution {
    public String solution(String rny_string) {
        StringBuffer str = new StringBuffer();
        for (int i = 0; i < rny_string.length(); i++){
            if (rny_string.charAt(i) == 'm'){
                str.append("rn");
            } else{
                str.append(rny_string.charAt(i));
            }
        }
        return str.toString();
    }
}