import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        List<Integer> answer = new LinkedList<>();
        HashMap<String, Integer> nameMap = new HashMap<>();
        
        for (int i=0; i<name.length; i++){
            nameMap.put(name[i], yearning[i]);
        }
        
        for (String[] people : photo){
            Integer score = 0;
            for(String person : people){
                score += nameMap.getOrDefault(person, 0);
            }
            answer.add(score);
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}