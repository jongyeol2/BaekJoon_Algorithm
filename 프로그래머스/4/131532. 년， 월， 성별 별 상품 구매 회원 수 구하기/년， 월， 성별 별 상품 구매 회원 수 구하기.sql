SELECT year(sales_date) as YEAR,
       month(sales_date) as MONTH,
       u.GENDER,
       count(distinct(o.user_id)) USERS
from user_info u
     join online_sale o
     on u.user_id = o.user_id
where gender is not NULL
group by 1,2,3
order by 1,2,3