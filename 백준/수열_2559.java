package 백준;

import java.util.Queue;
import java.util.LinkedList;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class 수열_2559 {
    public static void main(String[] args){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try{
            String[] inputLine = reader.readLine().split(" ");
            int N = Integer.parseInt(inputLine[0]);
            int K = Integer.parseInt(inputLine[1]);

            String[] Numbers = reader.readLine().split(" ");

            Queue<Integer> queue = new LinkedList<>();

            int Total = 0;
            int Max = -100 * N;
            for (int i = 0; i < N; i++){
                queue.offer(Integer.parseInt(Numbers[i]));
                Total += Integer.parseInt(Numbers[i]);
                if (queue.size() > K){
                    Total -= queue.poll();
                }
                if (queue.size() == K && Total > Max){
                    Max = Total;
                }
            }
            System.out.println(Max);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
