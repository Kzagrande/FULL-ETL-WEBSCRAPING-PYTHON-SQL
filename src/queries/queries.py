INSERT_SORTING_IN = '''
    INSERT INTO sorting_in
        (package_number, warehouse, order_number, shipping_mode, recomendation_zone, recomendation_lane, operated_by, operation_time, sector)
    VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

