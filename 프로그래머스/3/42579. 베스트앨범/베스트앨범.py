import heapq

def solution(genres, plays):
    genreTotalPlays = {}
    genreSongs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genreTotalPlays[genre] = genreTotalPlays.get(genre, 0) + play
        
        if genre not in genreSongs:
            genreSongs[genre] = []
        heapq.heappush(genreSongs[genre], (-play, i))

    sortedGenres = sorted(genreTotalPlays.items(), key=lambda item: item[1], reverse=True)

    answer = []
    for genre, total in sortedGenres:
        for _ in range(2):
            if genreSongs[genre]:
                play, index = heapq.heappop(genreSongs[genre])
                answer.append(index)
            else:
                break
                
    return answer