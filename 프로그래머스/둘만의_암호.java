package 프로그래머스;

public class 둘만의_암호 {
    public static void main(String[] args){
        String s = "aukks";
        String skip = "wbqd";
        int index = 5;
        System.out.println(solution(s,skip,index));
    }
    public static String solution(String s, String skip, int index) {
        String answer = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            for (int j = 0; j < index; j++) {
                c += 1;
                if (c > 'z') {
                    c -= 26;
                }
                if (skip.contains(String.valueOf(c))) {
                    j--;
                }
            }
            answer += c;
        }

        return answer;
    }
}
