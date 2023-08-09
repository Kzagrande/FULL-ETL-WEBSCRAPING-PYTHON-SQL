import sys 
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.drivers.google_sheet.google_sheet_getter import GoogleSheetGetter
from src.stages.extract.extract_scheduling import ExtractScheduling
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

def test_extract():
    get_sheet_getter = GoogleSheetGetter(spreadsheet_id='1LuRAClLK05tTGqlWBRwCou8bPGrcyJMyNICoXQpDqws')
    
    extract_schaduling = ExtractScheduling(get_sheet_getter)
    response = extract_schaduling.extract()
    print()
    print(response)
    
    assert isinstance(response,ExtractContract)
    
    
def test_extract_error():
    get_sheet_getter = 'ERRO'

    extract_schaduling = ExtractScheduling(get_sheet_getter)
    
    try:
        extract_schaduling.extract()
    except Exception as exception:
        assert isinstance(exception,ExtractError)    
