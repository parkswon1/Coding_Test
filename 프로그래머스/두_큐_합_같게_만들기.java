package 프로그래머스;

import java.util.*;
public class 두_큐_합_같게_만들기 {
    public static void main(String[] args){
        System.out.println(solution(new int[]{3, 2, 7, 2}, new int[]{4,6,5,1}));
    }

    public static int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long que1Value = 0;
        long que2Value = 0;
        Queue<Integer> que1 = new LinkedList<>();
        Queue<Integer> que2 = new LinkedList<>();
        for (int i = 0; i < queue1.length; i++){
            que1.add(queue1[i]);
            que1Value += queue1[i];
            que2.add(queue2[i]);
            que2Value += queue2[i];
        }

        while(true) {
            if (que1Value > que2Value){
                int temp = que1.poll();
                que1Value -= temp;
                que2Value += temp;
                que2.add(temp);
            } else if (que1Value < que2Value) {
                int temp = que2.poll();
                que2Value -= temp;
                que1Value += temp;
                que1.add(temp);
            } else{
                return answer;
            }
            answer += 1;
            if (answer > 600000){
                return -1;
            }
        }
    }
}
