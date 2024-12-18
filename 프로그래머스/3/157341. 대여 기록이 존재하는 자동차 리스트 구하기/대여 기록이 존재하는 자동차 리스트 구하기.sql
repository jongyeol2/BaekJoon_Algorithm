SELECT distinct(c.car_id)
from CAR_RENTAL_COMPANY_CAR c
     left join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.car_id = h.car_id
where c.car_type = '세단' and h.start_date like '2022-10%'
order by 1 desc
