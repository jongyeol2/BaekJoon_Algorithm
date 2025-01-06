# SELECT c.car_id,
#        c.car_type,
#        round(daily_fee * 30*(100-discount_rate)/100) FEE
# from CAR_RENTAL_COMPANY_CAR c
# join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
#      on c.car_id = h.car_id
# join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
#      on c.car_type = d.car_type 
# where c.car_type in ('세단', 'SUV')
#       and d.duration_type = '30일 이상'
#       and (start_date >= '2022-12-01' or end_date < '2022-11-01')
# having FEE between 500000 and 1999999
# order by 3 desc, 2, 1 desc

SELECT 
    C.CAR_ID,
    C.CAR_TYPE,
    FLOOR(C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR C
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN D 
    ON C.CAR_TYPE = D.CAR_TYPE
WHERE 
    C.CAR_TYPE IN ('세단', 'SUV')
    AND D.DURATION_TYPE = '30일 이상'
    AND C.CAR_ID NOT IN (
        SELECT CAR_ID 
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
    )
HAVING 
    FEE BETWEEN 500000 AND 1999999
ORDER BY 
    FEE DESC, 
    CAR_TYPE ASC, 
    CAR_ID DESC;