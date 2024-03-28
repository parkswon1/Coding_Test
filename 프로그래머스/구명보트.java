package 프로그래머스;

import java.util.*;
public class 구명보트 {
    public static void main(String[] args){
        int[] people = {70, 80, 50};
        int limit = 100;
        System.out.println(solution(people,limit));
    }

    public static int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        Deque<Integer> peopleQue = new ArrayDeque<>();
        for (int i = 0; i < people.length; i++){
            peopleQue.add(people[i]);
        }
        while(peopleQue.size() > 1){
            int back = peopleQue.removeLast();
            if (back + peopleQue.getFirst() <= limit){
                peopleQue.removeFirst();
            }
            answer += 1;
        }

        if (peopleQue.size() == 1 && peopleQue.removeLast() <= limit){
            answer += 1;
        }

        return answer;
    }

}
