# Programmers SQL L1: 이름이 있는 동물의 아이디
# Date : 2021.01.25
# IS NULL

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID ASC;
