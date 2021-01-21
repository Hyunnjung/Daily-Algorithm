# CodeUp 기초100제 : 1082
# [기초-종합] 16진수 구구단?
# DATE : 2020.01.21

a = int(input(), 16) # 16진수 입력받음
b = hex(a)[2].upper()

for i in range(1, 16):
    c = hex(a*i) [2:].upper() # 곱한 값(2부터)
    d = hex(i)[2:].upper()
    print(b+"*"+d+"="+c)