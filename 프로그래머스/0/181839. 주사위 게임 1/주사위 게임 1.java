class Solution {
    public int solution(int a, int b) {
        boolean isOddA = a % 2 == 1;
        boolean isOddB = b % 2 == 1;
        
        if (isOddA && isOddB) {
            return (a * a) + (b * b);
        } else if (isOddA || isOddB) {
            return 2 * (a + b);
        } else { 
            return Math.abs(a - b);
        }
    }
}