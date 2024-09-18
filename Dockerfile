FROM arm32v7/python:3

# 安装必要的 Python 库
RUN pip3 install RPi.GPIO flask pytest pytest-mock requests pytest-cov

# 复制您的 API 代码到容器中
COPY . /app
WORKDIR /app

# 安装必要的 Python 库，包括本地包
RUN pip install -e .
RUN pip install -r requirements.txt

# 设置 PYTHONPATH
ENV PYTHONPATH="/app:${PYTHONPATH}"

# 暴露 API 端口
EXPOSE 80

# 运行 API
CMD ["pytest"]
