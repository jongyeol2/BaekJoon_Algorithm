SELECT car_id,
       round(avg(datediff(END_DATE, START_DATE) + 1), 1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by 1
having round(avg(datediff(END_DATE, START_DATE) + 1), 1) >= 7
order by 2 desc, 1 desc