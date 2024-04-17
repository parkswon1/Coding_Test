package 프로그래머스;

import java.util.*;

public class 베스트앨범 {
    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answerList = new ArrayList<>();
        Map<String, PriorityQueue<int[]>> genresMap = new HashMap<>();
        Map<String, Integer> totalPlaysMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            if (!genresMap.containsKey(genre)) {
                genresMap.put(genre, new PriorityQueue<>((a, b) -> b[0] - a[0]));
                totalPlaysMap.put(genre, 0);
            }

            genresMap.get(genre).offer(new int[]{play, i});
            totalPlaysMap.put(genre, totalPlaysMap.get(genre) + play);
        }

        List<String> sortedGenres = new ArrayList<>(totalPlaysMap.keySet());
        Collections.sort(sortedGenres, (a, b) -> totalPlaysMap.get(b) - totalPlaysMap.get(a));

        for (String genre : sortedGenres) {
            PriorityQueue<int[]> pq = genresMap.get(genre);
            for (int j = 0; j < 2 && !pq.isEmpty(); j++) {
                answerList.add(pq.poll()[1]);
            }
        }

        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int[] result = 베스트앨범.solution(genres, plays);
        System.out.println(Arrays.toString(result));
    }
}