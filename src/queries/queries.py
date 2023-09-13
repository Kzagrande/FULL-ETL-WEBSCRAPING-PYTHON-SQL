INSERT_SORTING_IN = """
    INSERT INTO sorting_in
        (warehouse, package_number,order_number,shipping_mode,recomendation_zone,recomendation_lane,operated_by,operation_time, sector,current_date_,extraction_hour)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

INSERT_PUTAWAY = """
    INSERT INTO putaway
        (warehouse,subpackage_number,order_number,zone_,lane,location,operated_by,operation_time,sector,current_date_,extraction_hour)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

INSERT_PICKING = """
    INSERT INTO picking
        (warehouse,picking_group_number,picking_task_number,picking_methods,type_,consolid_ord_num,subpackage_number,wheter_short_picking,picking_location,lane,picking_area,picking_container,status,create_by,task_criation_time,task_pick_up_time,picker,picking_time,voided_by,voided_time,flag_cancel,sector,current_date_,extraction_hour)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

INSERT_SORTING_OUT = """
    INSERT INTO sorting_out
        (warehouse,task_group_number,picking_container,picking_task_number,package_number,subpackage_number,basket_number,mark_box_empty_name,sorted_by,sorting_time,sector,current_date_,extraction_hour)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

INSERT_PACKING = """
    INSERT INTO packing
        (consolid_recomed_number,consolid_all_pack_number,subpackage_number,lack_parcels_packing,workstation,operated_by,operation_time,sector,current_date_,extraction_hour,Warehouse)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

INSERT_BACKLOG = """
    INSERT INTO ware_ods_shein.sectors_backlog
    (sector,value, extraction_hour) 
    VALUES 
    (%s,%s,%s)
"""


INSERT_HC = """
    INSERT INTO hc
        (name,id_employ,admission_dt,company,warehouse,bz,coolar,category,sector,role_1,shift,schedule,manager_1,manager_2,manager_3,status,role_2,user_)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        
"""


# Isso aqui é um gato pois precisava passar algo para a query da classe
TRUNCATE_TABLE = """
"""

RUN_PROCEDURE = """
    CALL uph_staff();
"""

UPDATE_RPA_CONTROL = """
UPDATE ware_ods_shein.rpa_control SET status = 1 WHERE id = %s
"""

