import heapq

def solution(genres, plays):
    answer = []
    genresDict = {}
    for i in range(len(genres)):
        if genres[i] not in genresDict:
            genresDict[genres[i]] = {"heapq": [], "total": 0}
        heapq.heappush(genresDict[genres[i]]["heapq"], [-plays[i],i])
        genresDict[genres[i]]["total"] += plays[i]

    sorted_keys = sorted(genresDict, key=lambda x: genresDict[x]["total"], reverse=True)
    for key in sorted_keys:
        for j in range(2):
            if genresDict[key]["heapq"]:
                answer.append(heapq.heappop(genresDict[key]["heapq"])[1])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))