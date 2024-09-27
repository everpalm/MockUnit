# test_my_module.py
import logging

logger = logging.getLogger(__name__)


class TestMyClass:
    def test_fetch_data_success(self, my_class_instance, mock_requests_get):
        # 設置 mock 返回的響應
        logger.debug(f'\nmock_requests_get = {mock_requests_get}')
        mock_response = mock_requests_get.return_value
        logger.debug(f'\nmock_response = {mock_response}')
        mock_response.status_code = 200
        logger.debug('\nmock_response.status_code ='
                     f' {mock_response.status_code}')
        mock_response.json.return_value = {'key': 'value'}
        logger.debug('mock_response.json.return_value ='
                     f' {mock_response.json.return_value}')

        # 呼叫 fetch_data 方法
        result = my_class_instance.fetch_data('http://example.com')

        # 驗證 fetch_data 返回正確的結果
        assert result == {'key': 'value'}

        # 驗證 requests.get 方法被正確呼叫一次
        mock_requests_get.assert_called_once_with('http://example.com',
                                                  timeout=5)

    def test_fetch_data_failure(self, my_class_instance, mock_requests_get):
        # 設置 mock 返回的響應
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 404  # 模擬一個失敗的響應

        # 呼叫 fetch_data 方法
        result = my_class_instance.fetch_data('http://example.com')

        # 驗證 fetch_data 返回 None
        assert result is None
        # 驗證 requests.get 方法被正確呼叫一次
        mock_requests_get.assert_called_once_with('http://example.com',
                                                  timeout=5)
