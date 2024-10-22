class Solution {
    public int solution(int[] arr1, int[] arr2) {
        if (arr1.length > arr2.length){
            return 1;
        } else if (arr1.length < arr2.length){
            return -1;
        } else{
            int arr1Sum = 0;
            int arr2Sum = 0;
            
            for (int arr : arr1){
                arr1Sum += arr;
            }
            for (int arr : arr2){
                arr2Sum += arr;
            }
            
            if (arr1Sum > arr2Sum){
                return 1;
            } else if(arr1Sum == arr2Sum){
                return 0;
            }
        }
        return -1;
    }
}