import java.lang.*;

class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuffer answer = new StringBuffer("");
        for(String str : str_list){
            if(!str.contains(ex)){
                answer.append(str);
            }
        }
        return answer.toString();
    }
}