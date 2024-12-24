select a.author_id,
       a.author_name,
       b.category,
       sum(c.sum_sales *b.price) SALES
from BOOK b
join AUTHOR a
on b.author_id = a.author_id
join (SELECT book_id,
             sum(sales) sum_sales
      from BOOK_SALES 
      where sales_date like '2022-01%'
      group by 1
     ) c
on b.book_id = c.book_id
group by 1,3
order by 1, 3 desc
