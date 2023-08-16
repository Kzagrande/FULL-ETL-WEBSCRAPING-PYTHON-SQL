from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from src.errors.load_error import LoadError
from .load_sorting_in import LoadSorting_in

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_sorting_in_attribute = []

    def insert_sorting_in(self, data):
        self.insert_sorting_in_attribute.append(data)


def test_load():
    repo = RepositorySpy()
    load_data = LoadSorting_in(repo)

    load_data.load(transform_contract_mock)
    assert repo.insert_sorting_in_attribute == transform_contract_mock.load_content

def test_load_error():
    repo = RepositorySpy()
    load_data = LoadSorting_in(repo)

    try:
        load_data.load('Entrada Com Erro')
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, LoadError)
