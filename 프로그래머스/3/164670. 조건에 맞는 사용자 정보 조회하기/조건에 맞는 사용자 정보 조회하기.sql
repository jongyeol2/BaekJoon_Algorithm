SELECT u.user_id,
       u.nickname,
       concat(u.city,' ',  u.street_address1,' ', u.street_address2) '전체주소',
       concat(substring(u.tlno,1,3), '-' , substring(u.tlno,4,4), '-', substring(u.tlno,8)) '전화번호'
from USED_GOODS_USER u
     join(select writer_id
          from USED_GOODS_BOARD
          group by 1
          having count(board_id) >= 3
     ) b on u.user_id = b.writer_id 
order by 1 desc