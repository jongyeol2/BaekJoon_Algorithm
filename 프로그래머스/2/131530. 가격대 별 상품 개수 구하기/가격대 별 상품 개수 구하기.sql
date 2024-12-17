select (price - (price % 10000)) PRICE_GROUP,
       count(*) PRODUCTS
from product
group by 1
order by 1
