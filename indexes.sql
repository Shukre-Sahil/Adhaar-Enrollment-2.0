/* INDEXES */


-- For time based quereis
create index idx_enrollment_date
on enrollment(date);

-- For state level aggregation
create index idx_enrollment_state
on enrollment(state);

--  For district level analysis
create index idx_enrollment_district
on enrollment(district);

-- For pincode intensity queries
create index idx_enrollment_pincode
on enrollment(pincode);