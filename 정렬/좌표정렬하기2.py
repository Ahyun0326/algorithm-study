# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

def sort(point):

  sort_y = []
  for i in range(len(point)):
    # y 좌표 검사
    sort_y.append([point[i][0], point[i][1]])

  # y 값을 기준으로 오름차순 정렬
  sort_y.sort(key=lambda x:x[1])

  # y 값이 동일한 경우, x를 기준으로 오름차순 정렬
  result = []
  sort_y.sort(key = lambda x:(x[1], x[0]))
  
  result = sort_y
  
  return result

# 점의 개수 입력받기
n = int(input())

point = []
for i in range(n):
  point.append(list(map(int, input().split())))

# print(point)
point = sort(point)
for i in range(len(point)):
  for j in range(len(point[i])):
    print(point[i][j], end=' ')
  print()
