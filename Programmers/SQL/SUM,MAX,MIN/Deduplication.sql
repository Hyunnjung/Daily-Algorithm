# Programmers SQL L2: 중복 제거하기
# Date : 2021.01.26
# SUM, MAX, MIN

SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
