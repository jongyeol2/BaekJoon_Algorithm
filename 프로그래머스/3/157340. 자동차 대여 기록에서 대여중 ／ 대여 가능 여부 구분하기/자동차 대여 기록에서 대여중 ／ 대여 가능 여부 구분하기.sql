SELECT car_id,
       case when max(start_date <= '2022-10-16' and '2022-10-16' <= end_date)=1 then '대여중'
            else '대여 가능'
            end AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by 1
order by 1 desc