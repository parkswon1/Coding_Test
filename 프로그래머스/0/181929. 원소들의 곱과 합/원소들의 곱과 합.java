import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        int mix = 1;
        for (int num:num_list){
            sum += num;
            mix *= num;
        }
        
        if (sum * sum > mix){
            return 1;
        }
        return 0;
    }
}