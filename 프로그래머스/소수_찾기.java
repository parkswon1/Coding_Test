package 프로그래머스;

import java.util.HashSet;
import java.util.Set;

public class 소수_찾기 {
    static Set<Integer> set;
    static boolean[] visited = new boolean[7];
    public static void main(String[] args) {
        String numbers = "17";
        set = new HashSet<>();
        search(numbers, "", 0);
        int answer = set.size();
        System.out.println(answer);
    }
    static void search(String numbers, String num1, int count){
        if (count > numbers.length()){
            return;
        }

        for (int i = 0; i < numbers.length(); i++){
            if(!visited[i]) {
                String num2 = num1;
                num2 += numbers.charAt(i);
                if (Prime(Integer.parseInt(num2))){
                    set.add(Integer.parseInt(num2));
                }
                visited[i] = true;
                search(numbers, num2, count + 1);
                visited[i] = false;
            }
        }
    }

    static boolean Prime(int num){
        if (num < 2){
            return false;
        }else{
            for (int i = 2; i*i <= num; i++){
                if (num % i == 0){
                    return false;
                }
            }
            return true;
        }
    }
}
