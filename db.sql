CREATE DATABASE IF NOT EXISTS ods_shein;

CREATE TABLE IF NOT EXISTS `ods_shein.sched_putaway` (
	full_date_time VARCHAR(50) primary key,
	shift VARCHAR(50),
	sector VARCHAR(50),
	working_hours_percent INT,
	backlog FLOAT,
	productivity FLOAT,
	direct_labors_ceva INT,
	indirect_labores_ceva INT,
	daily_labors_productivity INT,
	daily_labors_indirect INT,
	total_labors INT,
	t4_t5_t6 INT,
	internal_sinergy INT,
	planned_throughput_per_hour FLOAT,
	real_throughput_per_hour FLOAT,
	real_productivity FLOAT,
	min_backlog FLOAT,
	max_baklog FLOAT
	
);

