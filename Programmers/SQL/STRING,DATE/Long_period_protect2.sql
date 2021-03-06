# Programmers SQL L3: 오랜 기간 보호한 동물2
# Date : 2021.01.28
# STRING,DATE

#ORACLE
SELECT ANIMAL_ID, NAME
    FROM (SELECT AI.ANIMAL_ID, AI.NAME
        FROM ANIMAL_INS AI, ANIMAL_OUTS AO
        WHERE AI.ANIMAL_ID = AO.ANIMAL_ID 
        ORDER BY AO.DATETIME - AI.DATETIME DESC)
    WHERE ROWNUM <= 2
    
    
#MYSQL
SELECT AI.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AS AI
JOIN ANIMAL_OUTS AS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY AO.DATETIME - AI.DATETIME DESC
LIMIT 2


# 다시 풀어보기
