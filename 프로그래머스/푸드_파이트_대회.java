package 프로그래머스;

import java.util.Stack;

public class 푸드_파이트_대회 {
    public static void main(String[] args){
        int[] food = {1,3,4,6};
        System.out.print(solution(food));
    }
    public static String solution(int[] food){
        Stack<String> backstack = new Stack<>();
        String answer = "";
        for (int i = 1; i < food.length; i++){
            int count = food[i]/2;
            for (int j = 0; j < count; j++){
                answer += Integer.toString(i);
                backstack.push(Integer.toString(i));
            }
        }
        answer += "0";
        while(!backstack.isEmpty()){
            answer += backstack.pop();
        }
        return answer;
    }
}
