class Solution {
    public int[] solution(int[] arr, int k) {
        if (k % 2 != 0) {
            for (int i = 0; i < arr.length; i++) {  // 조건문 수정
                arr[i] *= k;
            }
        } else {
            for (int i = 0; i < arr.length; i++) {  // 조건문 수정
                arr[i] += k;
            }
        }
        return arr;
    }
}