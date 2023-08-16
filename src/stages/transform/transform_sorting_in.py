import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract

class TransformSorting:
     
     def transform(self, extract_sorting: ExtractContract) -> TransformContract:
         transformed_data = self.__filter_and_transform_data(extract_sorting)
         transformed_data_contract = TransformContract(
             load_content=transformed_data
         )
         
         return transformed_data_contract

     
     def __filter_and_transform_data(self, extract_sorting: ExtractContract) -> pd.DataFrame:
         data_content = extract_sorting.raw_information_content
         data_content['sector'] = 'sorting_in'                   
         print(data_content)
         excel_file = "output.xlsx"
         data_content.to_excel(excel_file, index=False)
         return data_content
        


         
