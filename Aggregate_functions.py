#!/usr/bin/env python
# coding: utf-8

# В данном файле будет представлен код SQL, с кратким описанием задачи.

# Динамика трат клиентов
SELECT 
    BuyDate
    MIN(Rub) as MinCheck,
    MAX(Rub) as MaxCheck,
    AVG(Rub) as AvgCheck   
FROM checks
GROUP BY BuyDate
ORDER BY 
    BuyDate DESC
LIMIT 10

# Необходимо найти клиентов которые приносят большую прибыль. Сумма покупок от 10 000 рублей.
SELECT   
    UserID,
    SUM(Rub) as Revenue    
FROM checks
GROUP BY 
    UserID
HAVING
    Revenue > 10000
ORDER BY 
    UserID DESC   
LIMIT 10

# Представим, что к вам пришел менеджер с проблемой: 
# за последний месяц он наблюдает снижение выручки в некоторых регионах и 
# хочет определить возможную причину этого снижения. 
# Необходимо сгруппировать данные о выручке по странам и найти среди них топ-5 стран по величине выручки, 
# так как интереснее всего нам будет смотреть именно на данные этих стран.
SELECT      
    Country,
    SUM(UnitPrice * Quantity) AS Revenue
FROM retail
GROUP BY
    Country
ORDER BY
    Revenue DESC
LIMIT 5

# В качестве более подробного описания выручки по странам можно посмотреть, 
# каково среднее количество купленных товаров и средняя цена товара в покупках, 
# совершенных в определенной стране.
# Посчитайте среднее число купленных товаров по стране и среднюю цену товара, с
# группировав данные по странам и используя агрегирующую функцию, 
# и отсортируйте по убыванию средней цены товара.
# Значение 'Manual' ключают данные об удаленных из чека позициях. 
# Для получения правильного ответа такие строки необходимо отфильтровать.
SELECT 
    Country,
    AVG(Quantity) as AvgQuanitiy,
    AVG(UnitPrice) as AvgPrice   
FROM retail
GROUP BY Country
HAVING Description != 'Manual'
ORDER BY
    AvgPrice DESC

# Теперь посмотрим на динамику общей суммы выручки по месяцам.
# Значение 'Manual' ключают данные об удаленных из чека позициях. 
# Для получения правильного ответа такие строки необходимо отфильтровать.
SELECT
    SUM(UnitPrice * Quantity) AS Revenue,
    toStartOfMonth(InvoiceDate) AS MONTH_rev
FROM retail
GROUP BY
    MONTH_rev
HAVING
    Description != 'Manual'
ORDER BY
    Revenue DESC   
LIMIT 10

# Давайте посмотрим на динамику выручки от покупателей, которые в среднем покупают самые дорогие товары.  
# В качестве целевой метрики будем использовать среднюю цену купленного товара (UnitPrice), 
# данные посмотрим за март 2011 года.
# Значение 'Manual' ключают данные об удаленных из чека позициях. 
# Для получения правильного ответа такие строки необходимо отфильтровать.
SELECT
    CustomerID, 
    AVG(UnitPrice) as AvgPrice,
    toStartOfMonth(InvoiceDate) as date_info  
FROM retail
WHERE date_info = '2011-03-01'
GROUP BY
    CustomerID,
    date_info    
HAVING 
    Description != 'Manual'
ORDER BY
    AvgPrice DESC
LIMIT 100

# Как изменилось среднее, минимальное и максимальное количество купленного товара в стране 
# с наибольшей выручкой в течение последних месяцев?
# Значение 'Manual' ключают данные об удаленных из чека позициях. 
# Для получения правильного ответа такие строки необходимо отфильтровать.
SELECT      
    SUM(UnitPrice * Quantity) AS Revenue,
    toStartOfMonth(InvoiceDate) AS MONTH_rev,
    AVG(Quantity) AS Avg_q,
    MIN(Quantity) AS MIN_q,
    MAX(Quantity) AS MAX_q
FROM retail
WHERE 
    Description != 'Manual' and Country == 'United Kingdom'
GROUP BY
    MONTH_rev
HAVING 
    Quantity > 0
ORDER BY
    Avg_q DESC
LIMIT 30