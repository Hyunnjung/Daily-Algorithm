# CodeUp 기초100제 : 1019
# [기초-입출력] 연월일 입력받아 그대로 출력
# DATE : 2020.01.19

a,b,c=input().split('.')

print('%04d' % int(a), end='.') # 4칸 사용해 출력(한 자리 수인 경우 앞에 0을 붙여 출력)
print('%02d' % int(b), end='.')
print('%02d' % int(c))