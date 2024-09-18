import pytest
from my_suite.my_case import MyClass


@pytest.fixture
def my_class_instance():
    # 創建並返回 MyClass 的實例
    return MyClass()
