
def test_get_data_file(connector):
    """Ожидается получение атрибута data_file"""
    assert connector.data_file == 'tests/test_data/test_connector.json'
    connector.data_file = 'tests/test_data/test_connector2.json'
    assert connector.data_file == 'tests/test_data/test_connector2.json'


def test_connector(connector):
    """Ожидается добавление, фильтрация, удаление элементов из файла"""
    data_for_file = [{'id': 1, 'title': 'tet'}, {'id': 2}]
    connector.insert(data_for_file)
    assert connector.select({}) == data_for_file
    assert connector.select({'id': 2}) == [{'id': 2}]

    assert connector.delete({}) is None
    connector.delete({'id': 2})
    assert connector.select({}) == [{'id': 1, 'title': 'tet'}]
