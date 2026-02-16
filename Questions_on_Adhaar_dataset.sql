/* Descriptive Overview */

-- Q1 What is the total enrollment overall?

select sum(total_enrollment) as Overall_enrollment from enrollment;

--  Q2 Total enrollment by state (Ranking)

select 
	distinct state,
	sum(total_enrollment) as enrollments,
	rank() over(order by sum(total_enrollment) desc) as rank
from enrollment
group by 1
order by rank asc;


--  Q3 Enrollment Intensity Per Pincode
select 	
	pincode,
	sum(total_enrollment) as enrollments
from enrollment 
group by 1;


/* Comparative Analysis */
--  Q4 Which age group dominates overall?

select 
	sum(age_0_5) as less_than_5,
	sum(age_5_17) as bewteen_5_17,
	sum(age_18_greater) as more_than_18
from enrollment;

-- Percentage for all age groups
select	
	sum(age_0_5) *100/ sum(total_enrollment)  as percentage_1,
	sum(age_5_17) * 100/ sum(total_enrollment)  as percentage_2,
	sum(age_18_greater) * 100 / sum(total_enrollment)  as percentage_3
from enrollment;


--  Q5 Top 5 districts per state

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

/* Trend and Growth Analysis */
--  Q6 Yearly Trend

select 
	year,
	sum(total_enrollment) as enrollments
from enrollment
group by year;


--  Q7 Monthly Trend

select
	month,
	sum(total_enrollment) as enrollments
from enrollment
group by month;


-- Q8 Month over Month growth
SELECT month,
       SUM(total_enrollment) AS total,
       LAG(SUM(total_enrollment)) OVER (ORDER BY month) AS prev_month
FROM enrollment
GROUP BY month
ORDER BY month;


-- Q9 Districts showing growth over time

select 
	district,
	sum(total_enrollment) as enrollments,
	lag(sum(total_enrollment)) over( order by district) as growth_district
from enrollment
group by district
order by district

select * from enrollment