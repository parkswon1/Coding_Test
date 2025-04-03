import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> list = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();
        
        for (int del : delete_list) {
            set.add(del);
        }

        for (int a : arr) {
            if (!set.contains(a)) {
                list.add(a);
            }
        }

        return list.stream().mapToInt(i -> i).toArray();
    }
}