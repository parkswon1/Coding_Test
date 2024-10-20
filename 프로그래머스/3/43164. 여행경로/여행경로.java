import java.util.*;

class Solution {
    boolean[] visited;
    ArrayList<String> routes;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        int cnt = 0;
        visited = new boolean[tickets.length];
        routes = new ArrayList<>();
        
        dfs("ICN", "ICN", tickets, cnt);
        
        Collections.sort(routes);
        answer = routes.get(0).split(" ");
        
        return answer;
    }
    
    public void dfs(String start, String route, String[][] tickets, int cnt){
        if(cnt == tickets.length){
            routes.add(route);
            return;
        }
        
        for(int i=0; i<tickets.length; i++){
            if(start.equals(tickets[i][0]) && !visited[i]){
                visited[i] = true;
                dfs(tickets[i][1], route + " " + tickets[i][1], tickets, cnt + 1);
                visited[i] = false;
            }
        }
    }
}