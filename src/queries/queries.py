INSERT_SORTING_IN = '''
    INSERT INTO sorting_in
        (package_number,warehouse,order_number,shipping_mode,recomendation_zone,recomendation_lane,operated_by,operation_time, sector)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

INSERT_PUTAWAY = '''
    INSERT INTO putaway
        (warehouse,subpackage_number,order_number,zone_,lane,location,operated_by,operation_time,sector)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

INSERT_PICKING = '''
    INSERT INTO picking
        (warehouse,picking_group_number,picking_task_number,picking_methods,type_,consolid_ord_num,subpackage_number,wheter_short_picking,picking_location,lane,picking_area,picking_container,status,create_by,task_criation_time,task_pick_up_time,picker,picking_time,voided_by,voided_time,flag_cancel,sector)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''
