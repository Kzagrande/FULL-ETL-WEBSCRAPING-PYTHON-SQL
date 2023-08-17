import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List

class TransformPutaway:
     
     def transform(self, extract_putaway: ExtractContract) -> TransformContract:
         transformed_data = self.__filter_and_transform_data(extract_putaway)
         transformed_data_contract = TransformContract(
             load_content=transformed_data
         )
         print('transformed data -->>',transformed_data_contract)
         return transformed_data_contract

     
     def __filter_and_transform_data(self, extract_putaway: ExtractContract) -> List:
         data_content = extract_putaway.raw_information_content
         data_content['sector'] = 'putaway'                   
         print(data_content)
         excel_file = "putaway.xlsx"
         data_content.to_excel(excel_file, index=False)
         data_content_list  = data_content.values.tolist()
         return data_content_list
        

