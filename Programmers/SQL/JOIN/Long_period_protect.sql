# Programmers SQL L3: 오랜 기간 보호한 동물(1)
# Date : 2021.01.31
# JOIN

#ORACLE
SELECT *
FROM (SELECT a.NAME, a.DATETIME
      FROM ANIMAL_INS a LEFT JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
      WHERE b.ANIMAL_ID IS NULL
      ORDER BY a.DATETIME
     )
WHERE ROWNUM < 4;


* LEFT JOIN: 왼쪽 테이블을 기준으로 오른쪽 테이블을 조인

* ROWNUM
ROWNUM과 인라인뷰를 사용해 DATETIME을 내림차순 정렬하여 가장 상위 1개 값만 조회
rownum <= 10 : rownum이 10 이하인 정보 추출
rownum = 10 : rownum이 10인 정보 추출

#MySQL
SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS a LEFT JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.DATETIME
LIMIT 3;
