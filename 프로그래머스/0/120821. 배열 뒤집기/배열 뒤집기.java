class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        int j = 0;
        for (int num = num_list.length - 1; num >= 0; num--){
            answer[j] = num_list[num];
            j++;
        }
        return answer;
    }
}