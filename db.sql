CREATE TABLE IF NOT EXISTS `ods_shein.sorting_in` (
	package_number VARCHAR(50) primary key,
	warehouse VARCHAR(50),
	order_number VARCHAR(50),
	shipping_mode VARCHAR(50),
	recomendation_zone INT,
	recomendation_lane INT,
	operated_by VARCHAR(50),
	operation_time DATETIME NOT NULL,
	sector VARCHAR(50)
)	ENGINE=INNODB;

