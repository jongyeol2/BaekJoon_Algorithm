SELECT u.user_id,
       u.nickname,
       sum(b.price) TOTAL_SALES
from USED_GOODS_BOARD b
     left join USED_GOODS_USER u on b.writer_id = u.user_id
where b.status = 'DONE'
group by 1
having sum(b.price) >= 700000
order by 3
