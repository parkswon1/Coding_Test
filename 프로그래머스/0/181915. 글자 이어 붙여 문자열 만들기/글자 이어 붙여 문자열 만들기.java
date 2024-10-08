import java.util.*;

class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder answer = new StringBuilder();
        Arrays.stream(index_list).forEach(num -> answer.append(my_string.charAt(num)));
        return answer.toString();
    }
}