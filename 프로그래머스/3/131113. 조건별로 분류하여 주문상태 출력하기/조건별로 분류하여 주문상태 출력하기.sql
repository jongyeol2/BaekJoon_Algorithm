SELECT order_id,
       product_id,
       date_format(out_date,'%Y-%m-%d'),
       case when out_date <= '2022-05-01' then '출고완료'
            when out_date is null then '출고미정'
            else '출고대기'
       end     
from food_order
order by 1
