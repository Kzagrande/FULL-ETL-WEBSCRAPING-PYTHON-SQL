import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog


class TransformShipping:
    def transform(self, extract_sorting: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_sorting)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_sorting: ExtractContract) -> List:
        try:
            data_content = extract_sorting.raw_information_content
            data_content.iloc[:,11].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,14].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,17].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,16].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )

            data_content.iloc[:,18].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )

            data_content.iloc[:,20].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,22].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,24].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,25].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            
            data_content.fillna('', inplace=True)


            print(data_content.columns[27])
            data_content.iloc[:,0] = "BR_GRU_RC_A"
            data_content.iloc[:,27] = "Completed"
            

             
            data_content["sector"] = "shipping_time"
            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            
            print(data_content.iloc[0,25])
            # hours = data_content.iloc[0,25] #completion time
            # hours_date_type = datetime.strptime(hours, "%Y-%m-%d %H:%M:%S")
            # hours_date_type = hours_date_type.replace(minute=0, second=0, microsecond=0).replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(data_content)
            excel_file = "output.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content.replace(["N/A", "Não Disponível"], pd.NA, inplace=True)
            data_content_list = data_content.values.tolist()
            print(data_content_list)
            

            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Rc_management",error_code=18
            ) from exception
