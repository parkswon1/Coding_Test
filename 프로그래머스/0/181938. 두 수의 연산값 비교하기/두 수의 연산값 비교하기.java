class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int plus = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int sum = 2 * a * b;
        
        if (plus >= sum){
            return plus;
        }
        return sum;
    }
}