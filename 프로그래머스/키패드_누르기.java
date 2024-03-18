package 프로그래머스;

public class 키패드_누르기 {
    public static void main(String[] args){
        int[] numbers = {7,0,8,2,8,3,1,5,7,6,2};
        String hand = "left";
        System.out.println(solution(numbers,hand));
    }
    public static String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        int leftHand = 10;
        int rightHand = 12;
        for (int i = 0; i < numbers.length; i++){
            switch (numbers[i]){
                case 1,4,7:
                    answer.append('L');
                    leftHand = numbers[i];
                    break;

                case 3,6,9:
                    answer.append('R');
                    rightHand = numbers[i];
                    break;

                default:
                    if (numbers[i] == 0){
                        numbers[i] = 11;
                    }

                    int leftDiff = Math.abs(numbers[i] - leftHand)/3 + Math.abs(numbers[i] - leftHand)%3;
                    int rightDiff = Math.abs(numbers[i] - rightHand)/3 + Math.abs(numbers[i] - rightHand)%3;

                    if (rightDiff < leftDiff){
                        answer.append('R');
                        rightHand = numbers[i];

                    } else if (rightDiff == leftDiff) {
                        if (hand.equals("left")){
                            answer.append('L');
                            leftHand = numbers[i];
                        }else{
                            answer.append('R');
                            rightHand = numbers[i];
                        }

                    }else{
                        answer.append('L');
                        leftHand = numbers[i];
                    }
                    break;
            }
        }
        return answer.toString();
    }
}
