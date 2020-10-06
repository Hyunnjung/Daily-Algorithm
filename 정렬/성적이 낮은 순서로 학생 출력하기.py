n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 반환하여 저장
    array.append((input_data[0], int(input_data[1])))

# Key를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student:student[1])

for student in array:
    print(student[0], end=' ')
