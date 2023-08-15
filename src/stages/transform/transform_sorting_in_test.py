import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.mocks.extract_sorting_in_contract import extract_contract_mock
from src.stages.transform.transform_sorting_in import TransformSorting

def test_transform():
    transform_raw_data = TransformSorting()
    transform_raw_data.transform(extract_contract_mock)
    
