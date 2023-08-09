import sys 
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
from typing import List
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError

class TransformRawScheduling:
    
    def transform(self, extract_contract:ExtractContract) :
        try:
            transformed_information = self.__filter_and_transform_data(extract_contract)
            transformed_data_contract = TransformContract(
                load_content=transformed_information
            )
            
            return transformed_data_contract
        except Exception as exception:
            raise TransformError(str(exception)) from exception
            
    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> List:
        extraction_date  = extract_contract.extraction_date 
        data_content = extract_contract.raw_information_content
        # transform_information  = []
        # print(data_content[8])
        return data_content[8]
       
        
       