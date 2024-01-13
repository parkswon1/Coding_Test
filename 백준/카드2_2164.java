package 백준;

import java.util.LinkedList;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 카드2_2164{
    public static void main(String[] args){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try{
            Queue<Integer> queue = new LinkedList<>();
            int n = Integer.parseInt(reader.readLine());
            for (int i = 1; i <= n; i++){
                queue.offer(i);
            }

            while(queue.size() > 1){
                queue.poll();
                int frontN = queue.poll();
                queue.offer(frontN);
            }
            System.out.println(queue.poll());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
