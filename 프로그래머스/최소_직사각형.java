package 프로그래머스;

public class 최소_직사각형 {
    public static void main(String[] args){
        int[][] arr = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        System.out.println(solution(arr));
    }
    public static int solution(int[][] sizes) {
        int maxWidth = 0;
        int maxheight = 0;
        for (int i = 0; i < sizes.length; i++){
            maxWidth = Math.max(maxWidth, Math.max(sizes[i][0], sizes[i][1]));
            maxheight = Math.max(maxheight, Math.min(sizes[i][0], sizes[i][1]));
        }
        return maxheight * maxWidth;
    }
}
