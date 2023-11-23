import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog
from dateutil.parser import parse


class TransformSubpackageManagement:
    def transform(self, extract_subpackage: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_subpackage)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_subpackage: ExtractContract) -> List:
        try:
            data_content = extract_subpackage.raw_information_content

            data_content.iloc[:, 7].fillna(0, inplace=True)
            data_content.iloc[:, 8].fillna(0, inplace=True)
            data_content.iloc[:, 23].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:, 23].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )

            data_content.fillna("", inplace=True)
            data_content.iloc[:, 9] = data_content.iloc[:, 9].str.replace(
                ".*极兔-巴西.*", "Jitu-Brasil", regex=True
            )
            data_content.iloc[:, 9] = data_content.iloc[:, 9].str.replace(
                ".*巴西邮政.*", "brazil postal service", regex=True
            )



            print(data_content['Operation time'])

            data_content["sector"] = "subpack_management"
            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            print( data_content["current_date_"])
            
            data_content["Operation time"] = data_content["Operation time"].apply(lambda x: parse(x))
            print( data_content["Operation time"])
                
                
            # data_content['new_operation_time'] = datetime.datetime.strptime(data_content['Operation time'], "%d/%m/%Y").strftime("%Y-%m-%d")
            # print( data_content['new_operation_time'])
            
        
            
            hours = str(data_content.iloc[0,26])
            print(type(hours))
            print(hours)
            hours_date_type = datetime.strptime(hours, "%Y-%m-%d %H:%M:%S")
            print(type(hours_date_type))
            print(hours_date_type)
            hours_date_type = hours_date_type.replace(minute=0, second=0, microsecond=0).replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours_date_type
            
            # data_content.drop(columns=['Operation time'], inplace=True)
            # data_content['Operation time'] = format_time
            print(data_content['Operation time'])
            print( data_content["extraction_hour"])
            
            excel_file = "output.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func=" __filter_and_transform_data - Subpackage_management",
                error_code=16,
            ) from exception
