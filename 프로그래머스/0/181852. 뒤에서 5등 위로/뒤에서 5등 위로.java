import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);

        if (num_list.length <= 5) {
            return new int[0];
        }
        
        return Arrays.copyOfRange(num_list, 5, num_list.length);
    }
}