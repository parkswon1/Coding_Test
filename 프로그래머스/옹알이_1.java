package 프로그래머스;

public class 옹알이_1 {
    public static void main(String[] args){
        String[] babbling = {"ayaye", "uuuma", "ye", "yemawoo", "ayaa"};
        System.out.println(solution(babbling));
    }

    public static int solution(String[] babbling) {
        String[] says = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        for (String s: babbling){
            String word = "";
            for (int i = 0; i < s.length(); i++){
                word += s.charAt(i);
                for (String say : says){
                    if (say.equals(word)){
                        word = "";
                    }
                }
            }
            if (word.isEmpty()){
                answer += 1;
            }
        }
        return answer;
    }
}