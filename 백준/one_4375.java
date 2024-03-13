package 백준;
import java.util.Scanner;

public class one_4375 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        while (scan.hasNextInt()) {

            int num = scan.nextInt();
            int mod = 0;

            for(int i = 1;;i++){
                mod = (mod*10+1)%num;
                if(mod == 0) {
                    System.out.println(i);
                    break;
                }
            }

        }
    }
}