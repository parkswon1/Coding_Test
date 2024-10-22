import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);
        int listLength = num_list.length;
        return Arrays.copyOfRange(num_list, 0, 5);
    }
}