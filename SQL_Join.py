#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# В данном файле будут показанны примеры задач с Join`ами.


# In[ ]:


# У пользователя может быть два идентификатора – UserID и DeviceID. 
# В таблице checks есть только UserID, в остальных – только DeviceID. 
# Во вспомогательной таблице devices есть и UserID, и DeviceID. 
# Давайте с помощью JOIN дополним таблицу events (left) данными о UserID пользователей из таблицы devices (right).
# Для некоторых DeviceID не будет пары UserID из таблицы devices – подумайте, какой вид JOIN подойдет, 
# чтобы не потерять те строки, где DeviceID есть в events, но нет в devices.
# Укажите UserID из первой строки результирующей таблицы, используя сортировку по убыванию по полю DeviceID.
SELECT 
    l.AppPlatform AS AppPlatform,
    l.events AS events,
    l.EventDate AS EventDate,
    l.DeviceID AS DeviceID,
    r.UserID AS UserID
FROM 
    events AS l
FULL JOIN
    devices AS r
ON
    l.DeviceID = r.DeviceID
ORDER BY
    DeviceID DESC
LIMIT 10


# In[1]:


# Давайте проверим, пользователи пришедшие из какого источника совершили наибольшее число покупок. 
# В качестве ответа выберите название Source, юзеры которого совершили больше всего покупок.
SELECT
    count(a.UserID) AS UserID,
    c.Source AS Source
FROM
    checks AS a
JOIN
    devices AS b
ON
    a.UserID = b.UserID
JOIN
    installs AS c
on 
    b.DeviceID = c.DeviceID
GROUP BY Source
ORDER by
    UserID DESC
LIMIT 10


# In[ ]:


# Теперь выясним, сколько всего уникальных юзеров совершили покупки в нашем приложении.
# Объедините нужные таблицы, посчитайте число уникальных UserID для каждого источника (Source), 
# и в качестве ответа укажите число пользователей, пришедших из Source_7.
SELECT
    COUNT(DISTINCT a.UserID) AS UserID,
    c.Source AS Source
FROM
    checks AS a
JOIN
    devices AS b
ON a.UserID = b.UserID
JOIN
    installs AS c
ON b.DeviceID = c.DeviceID

GROUP BY
    Source
ORDER BY 
    Source DESC
LIMIT 10


# In[ ]:


# Выведите идентификаторы устройств пользователей, 
# которые совершили как минимум одну покупку за последний месяц (октябрь 2019). 
# Используйте сортировку по возрастанию DeviceID и укажите минимальное значение.
SELECT
    l.Rub AS Rub,
    toStartOfMonth(CAST(l.BuyDate  as date)) AS BuyDate,
    r.DeviceID AS DeviceID
FROM
    checks AS l
JOIN 
    devices AS r
ON
    l.UserID = r.UserID
WHERE
    BuyDate = '2019-10-01'
ORDER BY
    DeviceID ASC
LIMIT 10


# In[ ]:


# Проверим, сколько товаров в среднем просматривают пользователи с разных платформ, 
# и пришедшие из разных источников.
# Отсортируйте полученную табличку по убыванию среднего числа просмотров. 
SELECT
    a.Platform AS Platform,
    a.Source AS Source,
    AVG(b.events) AS events
FROM
    installs AS a
JOIN
    events AS b
ON
    a.DeviceID = b.DeviceID
GROUP BY
    Platform, Source
ORDER BY
    events DESC
LIMIT 50


# In[ ]:


# Давайте посчитаем число уникальных DeviceID в инсталлах, 
# для которых присутствуют просмотры в таблице events с разбивкой по платформам.
SELECT
    COUNT(DISTINCT l.DeviceID) AS DeviceID,
    l.Platform AS Platform,
    sum(r.events) AS events
FROM
    installs AS l
LEFT SEMI JOIN
    events AS r
ON
    l.DeviceID = r.DeviceID
WHERE
    Platform = 'android' 
GROUP BY
    Platform
ORDER BY
    DeviceID DESC
LIMIT 15


# In[ ]:


# Давайте теперь посчитаем конверсию из инсталла в просмотр 
# с разбивкой по платформе инсталла – в данном случае это доля DeviceID, 
# для которых есть просмотры, от всех DeviceID в инсталлах.
SELECT
    count(DISTINCT b.DeviceID) / count(DISTINCT a.DeviceID) AS DeviceID_conversion,
    a.Platform AS Platform
FROM
    installs AS a
LEFT JOIN
    events AS b
ON
    a.DeviceID = b.DeviceID
WHERE Platform = 'iOS'
GROUP BY
    Platform


# In[ ]:


# Нам надо отобрать примеры DeviceID из таблицы event, которых нет в таблице installs.
SELECT
    l.DeviceID AS DeviceID_table_l,
    r.DeviceID AS DeviceID_table_r
FROM 
    events AS l
LEFT ANTI JOIN
    installs AS r
ON
    l.DeviceID = r.DeviceID
ORDER BY
    DeviceID_table_l DESC
LIMIT 10


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




