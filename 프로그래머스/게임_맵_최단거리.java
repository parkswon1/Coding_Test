package 프로그래머스;

import java.util.ArrayDeque;
import java.util.Deque;

public class 게임_맵_최단거리 {
    public static void main(String[] args){
        int[][] maps = {{1,0,1,1,1},
                        {1,0,1,0,1},
                        {1,0,1,1,1},
                        {1,1,1,0,0},{
                        0,0,0,0,1}};
        System.out.println(solution(maps));
    }

    public static int solution(int[][] maps) {
        int N = maps[0].length;
        int M = maps.length;
        int[][] move = {{1,0},{-1,0},{0,1},{0,-1}};
        maps[0][0] = 0;
        Deque<Integer[]> que = new ArrayDeque<>();
        Integer[] start = {0,0,1};
        que.add(start);

        int x,y,z,my,mx,mz;
        while(!que.isEmpty()){
            Integer[] node = que.removeFirst();
            y = node[0];
            x = node[1];
            z = node[2];
            for (int[] mv:move){
                my = mv[0] + y;
                mx = mv[1] + x;
                mz = z + 1;
                if (0 <= my && my < M && 0 <= mx && mx < N){
                    if (my == M -1 && mx == N - 1){
                        return mz;
                    } else if (maps[my][mx] == 1) {
                        maps[my][mx] = 0;
                        Integer[] nextnode = {my,mx,mz};
                        que.add(nextnode);
                    }
                }
            }
        }
        return -1;
    }
}
