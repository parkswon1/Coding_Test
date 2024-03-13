package 백준;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 블로그_21921 {
    public static void main(String[] args){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try{
            String inputLine = reader.readLine();
            String[] inputTokens = inputLine.split(" ");
            int N = Integer.parseInt(inputTokens[0]);
            int X = Integer.parseInt(inputTokens[1]);

            Queue<Integer> queue = new LinkedList<>();
            String stringNumbers = reader.readLine();
            String[] Numbers = stringNumbers.split(" ");
            int total = 0;
            int max = 0;
            int count = 0;
            for (int i = 0; i < N; i++){
                int nowNumber = Integer.parseInt(Numbers[i]);
                queue.offer(nowNumber);
                total += nowNumber;
                if (queue.size() > X){
                    total -= queue.poll();
                }

                if (max < total) {
                    max = total;
                    count = 1;
                } else if (max == total){
                    count += 1;
                }
            }

            if (max == 0){
                System.out.println("SAD");
            } else {
                System.out.println(max);
                System.out.println(count);
            }
        }catch (IOException | NumberFormatException e){
            e.printStackTrace();
        }
    }
}
