FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

# 默认运行一个示例题目，可在 docker run 时覆盖命令执行其他题目。
CMD ["python", "1.两数之和.py"]
