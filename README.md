# CI Demo Django 项目

这是一个简单的 Django 示例项目，用于展示 CI/CD 流程和基本的 Django 应用开发。

## 项目概述

本项目是一个基础的 Django Web 应用，提供了简单的健康检查和系统信息 API 接口。适合作为 CI/CD 流程示例或 Django 入门学习使用。

## 技术栈

- Python 3.x
- Django 5.2
- Gunicorn 23.0.0 (WSGI HTTP 服务器)
- SQLite (开发环境数据库)

## 功能特性

- 基础的"Hello World"页面
- 健康检查 API 接口 (`/healthz`)
- 系统信息 API 接口 (`/info`)
- 配置好的 Django 项目结构

## 安装与设置

### 先决条件

- Python 3.x
- pip (Python 包管理器)

### 安装步骤

1. 克隆仓库：

```bash
git clone <仓库URL>
cd ci-demo-django
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 运行数据库迁移：

```bash
python manage.py migrate
```

4. 启动开发服务器：

```bash
python manage.py runserver
```

现在，您可以在浏览器中访问 `http://127.0.0.1:8000` 来查看应用。

## API 接口

### Hello World

- URL: `/hello/`
- 方法: GET
- 响应: "Hello, World!"

### 健康检查

- URL: `/healthz/`
- 方法: GET
- 响应: JSON 格式的健康状态信息

### 系统信息

- URL: `/info/`
- 方法: GET
- 响应: JSON 格式的应用和环境信息

## 生产环境部署

使用 Gunicorn 作为 WSGI HTTP 服务器进行部署：

```bash
gunicorn demo.wsgi:application
```

## 项目结构

```
ci-demo-django/
├── demo/              # 项目核心设置
├── hello/             # 示例应用
├── logs/              # 日志文件
├── db.sqlite3         # SQLite数据库
├── manage.py          # Django管理脚本
└── requirements.txt   # 项目依赖
```

## 贡献

欢迎提交问题和拉取请求来改进项目。

## 许可

[MIT License](LICENSE)
