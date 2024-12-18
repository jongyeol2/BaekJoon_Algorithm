SELECT food_type,
       rest_id,
       rest_name,
       max(favorites)
from REST_INFO 
where favorites in (
    select max(favorites)
    from rest_info
    group by food_type
)
group by 1
order by 1 desc