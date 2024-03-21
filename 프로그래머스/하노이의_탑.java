package 프로그래머스;
import java.util.*;

public class 하노이의_탑 {
    static int index = 0;
    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.println("Tower of Hanoi");
        System.out.print("Number of disks: ");
        int n = stdIn.nextInt();
        System.out.print(solution(n));
    }
    public static int[][] solution(int n) {
        int[][] answer = new int[(int) Math.pow(2, n) - 1][2];
        hano(n,1,3,2, answer);
        return answer;
    }

    public static void hano(int num, int now, int to, int ex, int[][] answer){
        if (num == 1){
            answer[index++] = new int[]{now, to};
            return;
        }
        hano(num - 1, now, ex, to, answer);
        answer[index++] = new int[]{now, to};
        hano(num - 1, ex, to, now, answer);
    }
}

