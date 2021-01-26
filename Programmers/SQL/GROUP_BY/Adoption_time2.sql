# Programmers SQL L4: 입양 시각 구하기2
# Date : 2021.01.26
# GROUP BY


SELECT A.HOUR, COUNT(B.DATETIME) AS COUNT
FROM (SELECT LEVEL-1 AS HOUR
          FROM DUAL
        CONNECT BY LEVEL <=24) A
LEFT JOIN ANIMAL_OUTS B
 ON A.HOUR = TO_CHAR(B.DATETIME,'HH24')
GROUP BY A.HOUR
ORDER BY A.HOUR

# 0~23까지의 값을 갖는 HOUR 칼럼 생성 -> 테이블A
# 테이블A와 입양정보 테이블 B를 HOUR를 사용해 LEFT JOIN
# 입양기록도 없는 시간도 조인 후 남아있어야 함 -> INNER JOIN x
# 값이 존재하는 경우만 집계 COUNT(B.DATETIME)
