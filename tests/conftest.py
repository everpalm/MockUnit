import logging
import pytest
from my_suite.my_case import MyClass

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s'
                    '%(message)s', datefmt='%Y-%m-%d %H:%M:%S')


@pytest.fixture(scope='module')
def my_class_instance():
    # 創建並返回 MyClass 的實例
    return MyClass()


@pytest.fixture
def mock_requests_get(mocker):
    # 正確地模擬 my_case 中的 requests.get 方法
    return mocker.patch('my_suite.my_case.requests.get')
