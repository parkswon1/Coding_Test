package 프로그래머스;

public class 모음_사전 {
    static String newword= "";
    static int result = 0;
    static final int N = 5;
    static String alpha = "AEIOU";
    public static void main(String[] args){
        String word = "AAAAE";
        dfs(word);
        System.out.println(result);
    }

    public static void dfs(String word){
        if (!word.equals(newword) && (newword.length() < 5)) {
                for (int i = 0; i < N; i ++){
                    StringBuilder sb;
                    sb = new StringBuilder(newword);
                    sb.append(alpha.charAt(i));
                    newword = sb.toString();
                    result += 1;
                    dfs(word);
                    if (word.equals(newword)) {
                        return;
                    }
                    newword = newword.substring(0,newword.length() - 1);
                }

        }
    }
}
