# my_module.py
import requests
from requests.exceptions import RequestException, JSONDecodeError


class MyClass:
    def fetch_data(self, url):
        try:
            response = requests.get(url, timeout=5)
            print('this is a test')

            # 檢查響應是否為 JSON 格式
            if response.status_code == 200:
                try:
                    return response.json()  # 返回 JSON 數據
                except JSONDecodeError:
                    print("Response is not a valid JSON")
                    return None
            else:
                print(f"Error: Received status code {response.status_code}")
                return None
        except RequestException as e:
            # 捕獲任何請求異常並返回錯誤信息
            print(f"An error occurred: {e}")
            return None
