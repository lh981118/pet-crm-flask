import sqlite3


conn = sqlite3.connect("pet_crm.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    wechat TEXT NOT NULL,
    city TEXT,
    budget TEXT,
    cat_type TEXT,
    message TEXT,
    status TEXT DEFAULT '新咨询',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("数据库和 customers 表创建成功！")