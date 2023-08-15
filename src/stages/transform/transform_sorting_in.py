import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from datetime import datetime, timedelta

class TransformSorting:
     
     def transform(self, extract_sorting: ExtractContract):
         transformed_data = self.__filter_and_transform_data(extract_sorting)
        #  self.__calculate_time_difference(transformed_data)
     
     def __filter_and_transform_data(self, extract_sorting: ExtractContract) -> pd.DataFrame:
        #  extraction_date = extract_sorting.extraction_date
         data_content = extract_sorting.raw_information_content
        #  data_content_frame = pd.DataFrame(data_content[1:], columns=data_content[0])
        #  data_content_frame['sector'] = 'sorting_in'     
        #  data_content_frame['操作时间'] = pd.to_datetime(data_content_frame['操作时间'])
        #  data_content_frame.sort_values(by='操作时间', ascending=True, inplace=True)  # Ordenar por '操作时间'
         excel_file = "output.xlsx"
         data_content.to_excel(excel_file, index=False)
         return data_content
        
    #  def __calculate_time_difference(self, data_frame: pd.DataFrame):
    #      data_frame['Diferença'] = data_frame['操作时间'].diff().apply(lambda x: x.total_seconds() if x < timedelta(minutes=10) else 0)
         
    #      print(data_frame)
    #      excel_file = "output.xlsx"
    #      data_frame.to_excel(excel_file, index=False)
         
# if __name__ == "__main__":
#     transform_sorting = TransformSorting()
#     transform_sorting.transform()
