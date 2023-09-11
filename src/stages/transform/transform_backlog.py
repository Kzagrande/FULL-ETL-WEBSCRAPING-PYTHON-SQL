import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog
from src.drivers.time_interval import get_current_and_last_hour
import pandas as pd
import sys
import pandas as pd
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog
from src.drivers.time_interval import get_current_and_last_hour

# Seu código anterior ...

class TransformBacklog:
    def transform(self, extract_backlog: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_backlog)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_picking: ExtractContract) -> List:
        try:
            data_content = extract_picking.raw_information_content

            hours = datetime.now()
            hours = hours.replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours

            # Crie uma lista de listas vazia
            data_list = []

            # Itere pelos dados do dicionário e adicione cada linha como uma lista
            for i in range(len(data_content["sector"])):
                value_float = float(data_content["value"][i].replace(",", ""))
                row = [
                    data_content["sector"][i],
                    value_float,
                    data_content["extraction_hour"],
                ]
                data_list.append(row)

            print(data_list)
            return data_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Backlog"
            ) from exception
