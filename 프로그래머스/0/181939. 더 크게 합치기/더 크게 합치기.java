class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int plus1 = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int plus2 = Integer.parseInt(String.valueOf(b) + String.valueOf(a));
        
        if (plus1 < plus2){
            return plus2;
        }
        return plus1;
    }
}