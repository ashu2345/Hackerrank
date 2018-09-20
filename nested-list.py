if __name__ == '__main__':
    students = []
    scores = []
    reqNames = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    students.sort()
    scores = list(set(scores))
    scores.sort()
    for student in students:
        if student[1] == scores[1]:
            print(student[0])
