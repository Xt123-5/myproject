# MyProject - Django 学习练习项目

一个基于 Django 的 Web 练习项目，涵盖模板渲染、ORM 增删改查、登录验证、第三方天气 API 调用等核心知识点。

## 技术栈

- **后端框架**：Django 4.2
- **前端**：HTML + Bootstrap 3.4.1 + jQuery 3.6.0
- **数据库**：SQLite3
- **第三方 API**：Open-Meteo 天气接口（调用成都实时天气）

## 项目结构

```
myproject/
├── manage.py              # Django 启动入口
├── app00/                 # 主应用
│   ├── models.py          # 数据模型（UserInfo、Department）
│   ├── views.py           # 视图函数
│   ├── urls.py            # 路由配置
│   ├── templates/         # HTML 模板
│   │   ├── login.html         # 登录页
│   │   ├── user_list.html     # 用户列表页
│   │   ├── user_add.html      # 用户添加页
│   │   ├── info_list.html     # 信息列表（ORM 查询）
│   │   ├── info_add.html      # 信息添加（ORM 插入）
│   │   ├── weather.html       # 天气展示页
│   │   └── tpl.html           # 模板语法演示
│   └── static/            # 静态资源（CSS/JS/图片）
└── myproject/             # 项目配置
    ├── settings.py        # 项目配置
    └── urls.py            # 全局路由
```

## 功能模块

| 路由 | 功能 |
|---|---|
| `/index/` | 首页欢迎页 |
| `/login/` | 登录验证（root / 123） |
| `/user/list` | 用户列表页面 |
| `/user/add` | 用户添加页面 |
| `/tpl/` | Django 模板语法演示（变量、列表、字典、循环） |
| `/weather/` | 调用 Open-Meteo API 显示成都实时天气 |
| `/something` | 重定向到百度 |
| `/orm/` | ORM 增删改查练习 |
| `/info/list/` | 从数据库读取用户信息并展示 |
| `/info/add/` | 表单提交新增用户到数据库 |
| `/info/delete/` | 根据 ID 删除数据库中的用户 |

## 数据模型

### UserInfo（用户信息表）
- name：用户名（最长 32 字符）
- password：密码（最长 64 字符）
- age：年龄（整数，默认 2）

### Department（部门表）
- title：部门名称（最长 16 字符）

## 运行方法

### 1. 安装依赖
```bash
pip install django requests
```

### 2. 初始化数据库
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 启动项目
```bash
python manage.py runserver
```

### 4. 浏览器访问
打开 http://127.0.0.1:8000/index/

## 仓库地址

- GitHub：https://github.com/Xt123-5/myproject
- SSH：`git@github.com:Xt123-5/myproject.git`

## 作者

- GitHub：[Xt123-5](https://github.com/Xt123-5)
