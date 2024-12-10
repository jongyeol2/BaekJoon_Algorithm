-- 코드를 입력하세요
SELECT fp.PRODUCT_ID,
       fp.PRODUCT_NAME,
       fp.PRICE * SUM(fo.AMOUNT)     
from FOOD_PRODUCT  fp
join FOOD_ORDER fo on fp.PRODUCT_ID = fo.PRODUCT_ID
where fo.PRODUCE_DATE like '2022-05%'
GROUP BY 1
ORDER BY 3 DESC, 1


