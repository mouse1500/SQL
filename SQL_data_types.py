#!/usr/bin/env python
# coding: utf-8

# Задание 1.
# Пользователи, сдающие квартиры на Airbnb, зарегистрировались в разное время. 
# Кто-то – очень давно, а кто-то совсем недавно. 
# Давайте проверим, в какой месяц и год зарегистрировалось наибольшее количество новых хостов. 
# В качестве ответа введите дату следующего формата: 2010-12
SELECT 
    COUNT(DISTINCT host_id) AS host,
    toStartOfMonth(toDateOrNull(host_since)) AS year_month

FROM listings

GROUP BY
    year_month

ORDER BY
    host DESC

LIMIT 100
# В качестве ответа использовать первую строку полученной таблицы


# Задание 2.
# Посмотрим на среднюю частоту ответа среди хозяев (f) и суперхозяев (t).
SELECT
    host_is_superhost,
    AVG(toInt32OrNull(replaceAll(host_response_rate, '%', ''))) as AvgResp
FROM
    (SELECT 
        DISTINCT host_id,
        host_is_superhost,
        host_response_rate
    FROM listings
    ) as sub
GROUP BY
    host_is_superhost
LIMIT 10
# Ответ:
# t  - 98
# f  - 89.39845065678679


# Задание 3.
# Сгруппируйте данные из listings по хозяевам (host_id) и посчитайте, 
# какую цену за ночь в среднем каждый из них устанавливает (у одного хоста может быть несколько объявлений). 
# Идентификаторы сдаваемого жилья объедините в отдельный массив. Таблицу отсортируйте по убыванию средней цены и 
# убыванию host_id (в таком порядке). В качестве ответа укажите первый массив в результирующей таблице, 
# состоящий более чем из двух id
SELECT
    host_id,
    groupArray(id) AS gr_id,
    AVG(toFloat32OrNull(replaceRegexpAll(price, '[$,]', ''))) as price_avg
FROM
    listings
GROUP BY
    host_id
ORDER BY
        price_avg DESC
LIMIT 10
# Ответ:
# 25757977, 25759146, 25802565, 25802651, 25802838, 25802909, 25803050, 25803117, 25803218, 25803260


# Задание 4.
# Посчитаем разницу между максимальной и минимальной установленной ценой у каждого хозяина.
# В качестве ответа укажите идентификатор хоста, у которого разница оказалась наибольшей. 
SELECT
    host_id,
    groupArray(id) AS gr_id,
    MAX(toFloat32OrNull(replaceRegexpAll(price, '[$,]', ''))) as price_max,
    MIN(toFloat32OrNull(replaceRegexpAll(price, '[$,]', ''))) as price_min,
    price_max - price_min AS difference
FROM
    listings
GROUP BY
    host_id
ORDER BY
    difference DESC
LIMIT 10
# Ответ
# 155140624


# Задание 5.
# Теперь сгруппируйте данные по типу жилья и выведите средние значения цены за ночь, 
# размера депозита и цены уборки. 
# Обратите внимание на тип данных, наличие значка $ и запятых в больших суммах. 
# Для какого типа жилья среднее значение залога наибольшее?
SELECT
    room_type,
    price,
    AVG(toFloat32OrNull(replaceRegexpAll(security_deposit, '[$,]', ''))) as deposit,
    cleaning_fee
FROM
    listings
GROUP BY
    room_type, price, cleaning_fee
ORDER BY
    deposit DESC
LIMIT 10
# Ответ:
# Entire home/apt


# Задание 6.
# В каких частях города средняя стоимость за ночь является наиболее низкой? 
# Сгруппируйте данные по neighbourhood_cleansed и посчитайте среднюю цену за ночь в каждом районе. 
# В качестве ответа введите название места, где средняя стоимость за ночь ниже всего.
SELECT
    neighbourhood_cleansed,
    AVG(toFloat32OrNull(replaceRegexpAll(price, '[$,]', ''))) AS price_avg
FROM
    listings
GROUP BY
    neighbourhood_cleansed
ORDER BY
    price_avg ASC
LIMIT 10
# Ответ:
# Neu-Hohenschönhausen Süd


# Задание 7.
# В каких районах Берлина средняя площадь жилья, которое сдаётся целиком, является наибольшей?
# Отсортируйте по среднему и выберите топ-3. 
SELECT
    neighbourhood_cleansed,
    AVG(toFloat32OrNull(square_feet)) AS square,
    room_type
FROM
    listings
GROUP BY
    neighbourhood_cleansed,
    room_type
ORDER BY
    square DESC
LIMIT 10
# Ответ:
# Lichtenrade, Kaulsdorf, Schöneberg-Süd


# Задание 8.
# Какая из представленных комнат расположена ближе всего к центру города. 
# В качестве ответа укажите id объявления.
SELECT
    room_type,
    id,
    geoDistance(13.4050, 52.5200, toFloat64OrNull(longitude), toFloat64OrNull(latitude)) AS range_geo
FROM
    listings
GROUP BY
    room_type,
    id,
    latitude,
    longitude
HAVING room_type = 'Private room'
ORDER BY range_geo ASC
LIMIT 10
# Ответ: 
# id - 19765058