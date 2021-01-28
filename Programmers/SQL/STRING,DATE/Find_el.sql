# Programmers SQL L2: 이름에 el들어가는 동물 찾기
# Date : 2021.01.28
# STRING,DATE

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE UPPER(NAME) LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME
