SELECT member_name,
       review_text,
       date_format(review_date,'%Y-%m-%d')
from MEMBER_PROFILE p
join REST_REVIEW r
on p.member_id = r.member_id
where p.member_id = (
    select member_id
    from REST_REVIEW
    group by member_id
    order by count(*) desc
    limit 1
)
order by 3, 2