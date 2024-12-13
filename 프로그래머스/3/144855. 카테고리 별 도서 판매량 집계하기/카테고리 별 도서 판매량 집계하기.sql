SELECT b.CATEGORY,
       sum(bs.SALES) TOTAL_SALES
from BOOK b
     left join BOOK_SALES bs on b.BOOK_ID = bs.BOOK_ID
where bs.SALES_DATE like "2022-01%"
GROUP BY 1
ORDER BY 1
