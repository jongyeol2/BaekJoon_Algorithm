SELECT month(start_date) as MONTH,
       car_id,
       count(car_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where start_date between '2022-08-01' and '2022-10-31'
      and car_id in (
          select car_id
          from CAR_RENTAL_COMPANY_RENTAL_HISTORY
          where start_date between '2022-08-01' and '2022-10-31'
          group by car_id
          having count(car_id) >= 5
      )
group by 1, 2
order by 1, 2 desc