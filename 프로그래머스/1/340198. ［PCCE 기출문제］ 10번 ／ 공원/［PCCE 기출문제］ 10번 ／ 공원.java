import java.util.*;
class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        
        for(int m : mats) {
          for(int i=0; i<park.length; i++) {
            for(int j=0; j<park[i].length; j++) {
                if(park[i][j].equals("-1")) {
                    if(matchSquare(i, j, m, park)) {
                      answer = Math.max(answer, m);  
                    } 
                }
            }
          }  
        }
        
        return answer;
    }
    
    private boolean matchSquare(int x, int y, int answer, String[][] park) {
       if(x+answer-1 >= park.length || y+answer-1 >= park[x].length) return false;
        
       for(int i=0; i<answer; i++) {
            for(int j=0; j<answer; j++) {
                String s = park[x+i][y+j];
                if(!s.equals("-1")) return false;    
            }
        } 
        
        return true;
    }
}