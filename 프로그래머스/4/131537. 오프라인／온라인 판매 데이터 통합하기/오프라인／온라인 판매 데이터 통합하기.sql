select date_format(sales_date, '%Y-%m-%d') SALES_DATE,
       product_id,
       user_id,
       sales_amount
from ONLINE_SALE  
where sales_date like '2022-03%'
union
select date_format(sales_date, '%Y-%m-%d') SALES_DATE,
       product_id,
       NULL as user_id,
       sales_amount
from OFFLINE_SALE 
where sales_date like '2022-03%'
order by 1, 2, 3