SELECT i.rest_id,
       i.rest_name,
       i.food_type,
       i.favorites,
       i.address,
       round(avg(r.review_score),2) SCORE
from REST_INFO i
     join rest_review r
     on i.rest_id = r.rest_id
where address like '서울%' 
group by 1
order by 6 desc, 4 desc