package 프로그래머스;

import java.util.*;
public class 올바른_괄호 {
    public static void main(String[] args){
        System.out.println(solution(")()("));
    }

    static boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (stack.isEmpty()){
                stack.push(c);
            }
            else {
                if (')' == c && stack.peek().equals('(')){
                    stack.pop();
                }else{
                    stack.push(c);
                }
            }
        }
        return stack.isEmpty();
    }
}