drop table if exists enrollment;
create table enrollment(
	Source_Name	varchar(100),
	date date,
	state varchar(50),
	district	varchar(100),
	pincode	int,
	age_0_5	int,
	age_5_17	int,
	age_18_greater int
);

-- Checking total number of rows --
select count(*) from enrollment;


-- Looking for null values --
select 
	*
from enrollment
where 
	age_0_5 is null and 
	age_5_17 is null and 
	age_18_greater is null;

-- No null values here


--  Checking for duplicates --

select 
	date, state, district, pincode, count(*)
from enrollment
group by 1,2,3,4
having count(*) > 1

-- Hence, duplicates exists here.


-- Add columns --
alter table enrollment
add column total_enrollment int;

select * from enrollment;

update enrollment
set total_enrollment = age_0_5 + age_5_17 + age_18_greater;


-- Remove unwanted columns --

alter table enrollment
drop column source_name;

select * from enrollment;


-- Add a column of 'Year' and 'Month' --

alter table enrollment
add column year int;

update enrollment
set year = extract(year from date);


alter table enrollment
add column month int;

update enrollment
set month = extract(month from date);

select * from enrollment;