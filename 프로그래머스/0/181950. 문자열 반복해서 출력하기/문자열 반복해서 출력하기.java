import java.util.Scanner;
import java.lang.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        
        String[] parts = input.split(" ");
        String inputStr = parts[0];
        int count = Integer.parseInt(parts[1]);
        
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < count; i++) {
            sb.append(inputStr);
        }
        System.out.println(sb.toString());
    }
}