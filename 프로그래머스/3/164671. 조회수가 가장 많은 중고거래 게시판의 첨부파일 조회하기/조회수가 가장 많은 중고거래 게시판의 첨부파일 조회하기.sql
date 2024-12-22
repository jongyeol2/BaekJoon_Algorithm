SELECT concat('/home/grep/src/',f.board_id, '/', f.file_id, f.file_name, f.file_ext)
from USED_GOODS_BOARD b
     left join USED_GOODS_FILE f
     on b.board_id = f.board_id
where b.views = (select max(views)
                 from USED_GOODS_BOARD)
order by f.file_id desc
