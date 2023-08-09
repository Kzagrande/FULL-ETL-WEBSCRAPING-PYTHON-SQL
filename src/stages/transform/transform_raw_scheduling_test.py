import sys 
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.transform.transform_raw_scheduling import TransformRawScheduling
from src.stages.contracts.mocks.extract_scheduling_contract import extract_scheduling_contract_mock
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError



def test_transform():
    tansform_raw_data = TransformRawScheduling()
    transformed_data_contract =  tansform_raw_data.transform(extract_scheduling_contract_mock)
    
    assert isinstance(transformed_data_contract, TransformContract)
    
    
    
def test_transform_error():
    tansform_raw_data = TransformRawScheduling()
    
    try:  
        tansform_raw_data.transform('Etntrada com erro')
    except  Exception as excption:
        assert isinstance(excption,TransformError) 
