import pytest

@pytest.fixture
def add_print():
    '''
    Глобальная фикстура говорит тебе, что ты умничка
    '''
    print('You are absolutely cool!')

@pytest.fixture(scope="function")
def fixture_for_collect_function(request):
    print(f'Это фикстура со scope="{request.scope}", она импортирует collections')
    def import_collect():
        import collections
        return collections.Counter(first=1, second=3, third=6 )
    return import_collect

@pytest.fixture(scope="class")
def fixture_for_class(request):
    print(f'Это фикстура со scope="{request.scope}"')

@pytest.fixture(scope="module", autouse=True)
def autofixture_for_module(request):
    print(f'\n\nЭто написала фикстура, которая применяется автоматически к каждому {request.scope}')
