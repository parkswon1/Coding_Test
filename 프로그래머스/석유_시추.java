package 프로그래머스;

import java.util.*;

public class 석유_시추 {
    public int solution(int[][] land) {
        int answer = 0;
        Map<Integer, Integer> oilMount = new HashMap<>();
        int Y = land.length;
        int X = land[0].length;
        int mark = 1;
        int[][] move = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for (int y = 0; y < Y; y++) {
            for (int x = 0; x < X; x++) {
                if (land[y][x] == 1) {
                    mark++;
                    oilMount.put(mark, 1);
                    Queue<int[]> node = new LinkedList<>();
                    node.offer(new int[]{y, x});
                    land[y][x] = mark;

                    while (!node.isEmpty()) {
                        int[] n = node.poll();
                        for (int[] mv : move) {
                            int my = n[0] + mv[0];
                            int mx = n[1] + mv[1];
                            if (my >= 0 && my < Y && mx >= 0 && mx < X && land[my][mx] == 1) {
                                land[my][mx] = mark;
                                oilMount.put(mark, oilMount.getOrDefault(mark, 0) + 1);
                                node.offer(new int[]{my, mx});
                            }
                        }
                    }
                }
            }
        }

        for (int x = 0; x < X; x++) {
            Set<Integer> oilSet = new HashSet<>();
            for (int y = 0; y < Y; y++) {
                if (land[y][x] != 0) {
                    oilSet.add(land[y][x]);
                }
            }
            int count = 0;
            for (int oil : oilSet) {
                count += oilMount.get(oil);
            }
            answer = Math.max(answer, count);
        }

        return answer;
    }
}
