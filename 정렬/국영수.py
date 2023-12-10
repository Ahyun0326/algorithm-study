n = int(input())

# 학생의 이름. 국어, 영어, 수학 점수 입력
students = []
for i in range(n):
    student = input().split()
    students.append((student[0],int(student[1]),int(student[2]),int(student[3])))

# 국어 점수가 감소하는 순서로 정렬, 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
students = sorted(students, key=lambda x:(-x[1],x[2],-x[3],x[0]))

# 정렬된 학생의 이름 출력
for i in students:
    print(i[0])
