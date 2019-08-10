import pytest


def test_list_check():
    '''
    1. Тест проверяет, что длина списка равна восьми
    '''
    this_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert len(this_list) == 8, 'It is not eight here :('


def test_with_fixture(add_print):
    '''
    2. Тест проверяет, что конкатенация в питоне работает верно
    и применяет фикстуру, описанную в conftest.py
    '''
    string = 'conca' + 'tenation'
    assert string == 'concatenation', 'Your concatenation is bad'


@pytest.fixture
def inner_fixture(request):
    '''
    Местная фикстура считает 5*5 и выводит сообщение после завершения теста
    '''
    def final():
        again = 5 * 5
        print(f'Again {again}')
    request.addfinalizer(final)


def test_square_list(inner_fixture):
    '''
    3. Тест проверяет работу генератора списков, возводящего все элементы
    исходного списка в квадрат и применяет фикстуру, описанную в текущем модуле
    '''
    start_list = [1, 2, 3, 4]
    square_list = [i * i for i in start_list]
    assert square_list == [1, 4, 9, 16], 'Lists is not equal'


def test_its_tuple():
    '''
    4. Тест проверяет, что у кортежа тип "tuple"
    '''
    that_tuple = ('I', 'am', 'Alena')
    assert type(that_tuple) == tuple, 'It is not tuple'


def test_dict_for_qa(add_print):
    '''
    5. Тест создает словарь, проверяет, что по ключу 'qa'
    получено верное значение и тоже применяет фикстуру из conftest.py
    '''
    dictionary = {'dev': 'good', 'front': 'better', 'qa': 'the best'}
    assert dictionary.get('qa') == 'the best', 'Something went wrong, QA is the best'


def test_copy_dict():
    '''
    6. Тест создает копию заданного словаря и сравнивает ее с исходным словарем
    '''
    original_dict = {'first': 1, 'second': 2, 'third': 3}
    double_dict = original_dict.copy()
    assert original_dict == double_dict, 'Copying dictionaries dont work'


class TestWrapper:

    def test_sets(self, fixture_for_class):
        '''
        7. Тест проверяет корректность преобразования списка в множество
        '''
        that_list = [1, 2, 1, 1, 4, 5, 2, 2, 2, 2, 5]
        assert set(that_list) == {1, 2, 4, 5}, 'Transform list to set failed'

    def test_set_intersect(self):
        '''
        8. Тест проверяет пересечение двух множеств
        '''
        first_set = {5, 4, 3, 2}
        second_set = {1, 2, 3, 6, 7}
        assert first_set & second_set == {2, 3}, 'Intersection is wrong'


def test_collections(fixture_for_collect_function):
    '''
    9. Тест проверяет, что наиболее часто встречаемый элемент из коллекции определен верно
    '''
    collect = fixture_for_collect_function()
    assert collect.most_common(1) == [('third', 6)]


def test_last():
    '''
    10. Тест проверяет таблицу умножения, потому что фантазия для тестов закончилась
    '''
    assert 6 * 9 == 54, 'Результат расчета 6 * 9 неверный'
