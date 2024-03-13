package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IQ_Test_1111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] numbersString = br.readLine().split(" ");
        Integer[] numbers = new Integer[N];

        for (int i = 0; i < N; i++){
            numbers[i] = Integer.parseInt(numbersString[i]);
        }
        switch (N){
            case 1 :
                System.out.println("A");
                break;
            case 2 :
                Nis2(numbers);
                break;
            default:
                Biggerthan3(numbers, N);
        }
    }

    private static void Nis2(Integer[] numbers) {
        if (numbers[0].equals(numbers[1])){
            System.out.println(numbers[0]);
        }
        else {
            System.out.println("A");
        }
    }

    private static void Biggerthan3(Integer[] numbers, int N) {
        int a,b;
        if (numbers[0].equals(numbers[1])){
            a = 1;
            b = 0;
        }
        else {
            a = (numbers[2] - numbers[1]) / (numbers[1] - numbers[0]);
            b = numbers[1] - numbers[0] * a;
        }

        int i = 0;
        int output = 1;
        while(N -1 > i){
            if (numbers[i+1] != numbers[i] * a + b){
                output = 0;
                break;
            }
            i ++;
        }

        if (output == 1){
            System.out.println(numbers[N -1] * a + b);
        }
        else{
            System.out.println("B");
        }
    }
}
