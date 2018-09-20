def climbingLeaderboard(scores, alice):
    returnarray = []
    for ascore in alice:
        pos = 1
        for i in range(len(scores)):
            if scores[i]>ascore and scores[i]!=scores[i-1]:
                pos+=1
            elif ascore > scores[i]:
                break
        scores.append(ascore)
        scores.sort(reverse=True)
        returnarray.append(pos)
    return returnarray

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
result = climbingLeaderboard(scores, alice)
print(result)
