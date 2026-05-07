# Pet CRM Flask

这是一个使用 Python Flask + SQLite 开发的宠物客户管理 CRM 系统。

项目用于记录宠物咨询客户信息，支持客户新增、查看、状态修改和删除，适合用于学习 Flask 后端开发、SQLite 数据库操作和基础 Web 项目结构。

## 项目功能

- 首页展示
- 客户列表
- 新增客户
- 查看客户详情
- 修改客户状态
- 删除客户
- SQLite 数据库存储客户信息

## 技术栈

- Python
- Flask
- SQLite
- HTML
- CSS

## 项目结构

```text
pet_crm/
├── app.py
├── init_db.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── customers.html
│   ├── new_customer.html
│   └── customer_detail.html
└── static/
    └── style.css

数据库字段

customers 表字段：

id          客户 ID，自动递增
name        客户称呼
wechat      微信号
city        所在城市
budget      预算范围
cat_type    想养的猫
message     具体问题
status      客户状态
created_at  创建时间

本地运行方式
1. 创建虚拟环境
python3 -m venv .venv
2. 激活虚拟环境

Mac / Linux：

source .venv/bin/activate
3. 安装依赖
pip install -r requirements.txt
4. 初始化数据库
python init_db.py
5. 启动项目
python app.py

启动后浏览器访问：

http://127.0.0.1:5000
当前路由
/                                  首页
/customers                         客户列表
/customers/new                     新增客户
/customers/<id>                    客户详情
/customers/<id>/status/<status>    修改客户状态
/customers/<id>/delete             删除客户
学习目标

通过这个项目练习：

Flask 路由
HTML 模板渲染
表单提交
GET / POST 请求
SQLite 数据库
SQL 增删改查
项目结构整理

- GitHub 远程仓库管理