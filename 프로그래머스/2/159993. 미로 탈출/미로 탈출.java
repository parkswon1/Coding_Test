import java.util.Queue;
import java.util.LinkedList;

class Solution {
    static String[][] arr;
    static boolean[][] visit;
    static int[][] markingArr;
    static int[] dr = {0,1,0,-1}, dc = {1,0,-1,0}; //앞 아래 뒤 위
    static int startRow = 0, startCol=0;
    static int exitRow =0, exitCol = 0;
    static int leverRow = 0, leverCol = 0;
    static boolean isAccessLever = false, isAccessExit = false;
    static int n = 0, m = 0;
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        
        arr = new String[n][m];
        visit = new boolean[n][m];
        markingArr = new int[n][m];
        
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                String str = String.valueOf(maps[i].charAt(j));
                if(str.equals("E")) {
                    exitRow = i;
                    exitCol = j;
                }
                if(str.equals("S")) {
                    startRow = i;
                    startCol = j;
                }
                if(str.equals("L")) {
                    leverRow = i;
                    leverCol = j;
                }
                arr[i][j] = str;
            }
        }
        
        visit[startRow][startCol] = true;
        bfs(startRow, startCol, "lever");
        
        if(isAccessLever) {
            visit = new boolean[n][m];
            visit[leverRow][leverCol] = true;
            bfs(leverRow, leverCol, "exit");
        }
        if(isAccessLever && isAccessExit) {
            return markingArr[exitRow][exitCol];
        }else {
            return -1;
        }
    }
    private static void bfs(int row, int col, String str) {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(row, col));
        while(!q.isEmpty()) {
            Point point = q.poll();
            if(str.equals("lever") && visit[leverRow][leverCol]) {
                isAccessLever = true;
                return;
            } 
            if(str.equals("exit") && visit[exitRow][exitCol]) {
                isAccessExit = true;
                return;
            }
            for(int i=0; i<dr.length; i++) {
                int nr = point.row + dr[i];
                int nc = point.col + dc[i];
                
                if(nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
                if(!arr[nr][nc].equals("X") && !visit[nr][nc]) {
                    markingArr[nr][nc] = markingArr[point.row][point.col] + 1;
                    visit[nr][nc] = true;
                    q.add(new Point(nr,nc));
                }
            }
        }
    }
    static class Point {
        int row;
        int col;
        Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}