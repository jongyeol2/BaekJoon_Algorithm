-- 코드를 입력하세요
SELECT PT_NAME,
       PT_NO,
       GEND_CD,
       AGE,
       if(TLNO is NULL, "NONE", TLNO) TLNO
FROM PATIENT
WHERE age <= 12
      AND GEND_CD = "W"
ORDER BY age DESC, PT_NAME