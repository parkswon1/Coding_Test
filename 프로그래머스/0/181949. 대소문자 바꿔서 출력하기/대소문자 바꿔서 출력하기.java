import java.util.Scanner;
import java.lang.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuffer sr = new StringBuffer(sc.next());
        for (int i = 0; i < sr.length(); i++) {
            char c = sr.charAt(i);
            if (Character.isUpperCase(c)) {
                sr.setCharAt(i, Character.toLowerCase(c));
            } else if (Character.isLowerCase(c)) {
                sr.setCharAt(i, Character.toUpperCase(c));
            }
        }
        
        System.out.println(sr.toString());
    }
}