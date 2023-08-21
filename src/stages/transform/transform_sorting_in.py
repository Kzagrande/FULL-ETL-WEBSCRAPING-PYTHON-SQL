import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime

class TransformSorting:
     
     def transform(self, extract_sorting: ExtractContract) -> TransformContract:
         transformed_data = self.__filter_and_transform_data(extract_sorting)
         transformed_data_contract = TransformContract(
             load_content=transformed_data
         )
         print('transformed data -->>',transformed_data_contract)
         return transformed_data_contract

     
     def __filter_and_transform_data(self, extract_sorting: ExtractContract) -> List:
         data_content = extract_sorting.raw_information_content
         columns_to_fill = ['Warehouse','Package No.','Order No.','Shipping Mode','Recommendation Zone','Recommendation Lane', 'Operated By']
         data_content["Operating time"].fillna(datetime(1500, 1, 11, 11, 11, 11), inplace=True) 
         data_content[columns_to_fill] = data_content[columns_to_fill].fillna("-")
         data_content['sector'] = 'sorting_in'                   
         print(data_content)
         excel_file = "output.xlsx"
         data_content.to_excel(excel_file, index=False)
         data_content_list  = data_content.values.tolist()
         return data_content_list
        


         
