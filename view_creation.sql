/* VIEWS CREATION*/


-- Q1 What is the total enrollment overall?

create or replace view v_total_enrollment as
select sum(total_enrollment) as Overall_enrollment from enrollment;



--  Q2 Total enrollment by state (Ranking)

create or replace view v_state_total_enrollment as
select 
	distinct state,
	sum(total_enrollment) as enrollments,
	rank() over(order by sum(total_enrollment) desc) as rank
from enrollment
group by 1
order by rank asc;


--  Q3 Enrollment Intensity Per Pincode

create or replace view v_intensity_per_pincode as 
select 	
	pincode,
	sum(total_enrollment) as enrollments
from enrollment 
group by 1;



--  Q4 Which age group dominates overall?


create or replace view v_age_group_dominates as 
select 
	sum(age_0_5) as less_than_5,
	sum(age_5_17) as bewteen_5_17,
	sum(age_18_greater) as more_than_18
from enrollment;


-- Percentage for all age groups
create or replace view v_percentage_age_group_dominates as 
select	
	sum(age_0_5) *100/ sum(total_enrollment)  as percentage_1,
	sum(age_5_17) * 100/ sum(total_enrollment)  as percentage_2,
	sum(age_18_greater) * 100 / sum(total_enrollment)  as percentage_3
from enrollment;


--  Q5 Top 5 districts per state

create or replace view v_top_5districts_per_state as
select * 
from (
select 
	state,
	district,
	sum(total_enrollment) as enrollments,
	rank() over(partition by state order by sum(total_enrollment) desc) as rank
from enrollment
group by 1,2
)
where rank <=5;




--  Q6 Yearly Trend

create or replace view v_yearly_trend as
select 
	year,
	sum(total_enrollment) as enrollments
from enrollment
group by year;


--  Q7 Monthly Trend


create or replace view v_monthly_trend as
select
	month,
	sum(total_enrollment) as enrollments
from enrollment
group by month;


-- Q8 Month over Month growth

create or replace view v_monthly_growth as
SELECT month,
       SUM(total_enrollment) AS total,
       LAG(SUM(total_enrollment)) OVER (ORDER BY month) AS prev_month
FROM enrollment
GROUP BY month
ORDER BY month;


-- Q9 Districts showing growth over time


create or replace view v_district_growth_rate as
select 
	district,
	sum(total_enrollment) as enrollments,
	lag(sum(total_enrollment)) over( order by district) as growth_district
from enrollment
group by district
order by district;


select * from v_total_enrollment;
select * from v_state_total_enrollment;
select * from v_intensity_per_pincode;
select * from v_age_group_dominates;
select * from v_percentage_age_group_dominates;
select * from v_top_5districts_per_state;
select * from v_yearly_trend;
select * from v_monthly_trend;
select * from v_monthly_growth;
select * from v_district_growth_rate;