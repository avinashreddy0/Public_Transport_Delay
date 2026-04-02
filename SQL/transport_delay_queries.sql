create database transport
use transport

select * from transport

--1 Find the average delay in each city.
select traffic_level,avg(DELAY_MINUTES) AS average_dealy
from transport
group by CITY
order by average_dealy desc

--2 Average delay by traffic level
select traffic_level,avg(DELAY_MINUTES) AS average_dealy
from transport
group by traffic_level
order by average_dealy desc

-- 3 Delay during rush hours

select rush_hour,avg(DELAY_MINUTES) AS average_dealy
from transport
group by rush_hour
order by average_dealy desc

-- 4 Weather impact on delayselect * from transport
select avg(delay_minutes) as AVG_DELAY,AVG(RAINFALL_MM) AS AVG_RAINFALL
FROM transport

-- task 5 vehicle type vs delay

select vehicle_type,avg(DELAY_MINUTES) AS average_dealy
from transport
group by vehicle_type 

-- task 6 Event impact on delays
select event_today,event_type,avg(delay_minutes) as avg_delay
from transport 
group by event_today,event_type

-- task 7 Top 5 routes with highest delay

select route_id,avg(delay_minutes) as avg_delay
from transport
group by route_id
order by avg_delay desc
limit 5

-- task 8 Delay by day of week

select  day_of_week,avg(delay_minutes) as avg_dealy
from transport
group by day_of_week
order by avg_dealy desc

-- task 9 Delay by hour of day

select hour,avg(delay_minutes) as avg_delay
from transport
group by hour
order by avg_delay desc

-- task 10 
select city,avg(delay_minutes) as avg_delay,rainfall_mm
from transport
where rainfall_mm > 5
group by city,rainfall_mm
order by avg_delay desc


select * from transport

update transport 
set event_type = 'IPL_match'
where event_type is null

update transport 
set traffic_level = replace( traffic_level,'###','')


set sql_safe_updates = 1