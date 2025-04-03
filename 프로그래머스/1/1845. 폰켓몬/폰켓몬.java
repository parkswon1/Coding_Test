import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }
        if (nums.length /2 < set.size()) { 
            return nums.length / 2;
        }
        return set.size();
    }
}