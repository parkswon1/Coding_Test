class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for (int arr : array){
            if (arr > height){
                answer++;
            }
        }
        return answer;
    }
}