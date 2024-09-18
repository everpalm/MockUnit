# test_my_module.py
import logging

logger = logging.getLogger(__name__)


class TestMyClass:
    def test_fetch_data_success(self, my_class_instance):
        # 呼叫 fetch_data 方法
        result = my_class_instance.fetch_data(
            'https://jsonplaceholder.typicode.com/posts/1')
        logger.debug(f'result = {result}')
        # 驗證 fetch_data 返回正確的結果
        assert result == {'userId': 1,
                          'id': 1,
                          'title':
                          'sunt aut facere repellat provident occaecati'
                          ' excepturi optio reprehenderit', 'body': 'quia et'
                          ' suscipit\nsuscipit recusandae consequuntur'
                          ' expedita et cum\nreprehenderit molestiae ut ut'
                          ' quas totam\nnostrum rerum est autem sunt rem'
                          ' eveniet architecto'}

    def test_fetch_data_failure(self, my_class_instance, mock_requests_get):
        # 呼叫 fetch_data 方法
        result = my_class_instance.fetch_data('http://example.com')

        # 驗證 fetch_data 返回 None
        assert result is None
