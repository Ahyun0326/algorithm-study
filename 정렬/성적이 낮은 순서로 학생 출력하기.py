n = int(input())

students = []
# 학생의 이름, 점수를 입력 받아 students 리스트에 저장
for i in range(n):
    student = input().split()
    # 점수는 정수형으로 변환해 추가하기
    students.append([student[0], int(student[1])])

# sorted와 lambda를 이용해 점수를 기준으로 students 리스트 정렬
answer = sorted(students, key=lambda x:x[1])
print(answer)




