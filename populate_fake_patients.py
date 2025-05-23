# Step 1: 新建一个文件 - 保存为 populate_fake_patients.py（与你的 main.py 同级）
# 文件结构应如下：
# omop-navigator-v3/
# ├── app/
# ├── data/
# ├── remote_nodes/
# ├── main.py
# └── populate_fake_patients.py ⬅️ 就是它

import sqlite3

def populate_fake_patients(db_path: str, num_patients: int):
    """
    向指定 SQLite 数据库中批量插入 person 表测试数据。
    如果表不存在则创建，避免重复插入。
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS person (person_id INTEGER PRIMARY KEY, year_of_birth INTEGER)")
    for i in range(2, num_patients + 2):
        cur.execute(
            "INSERT INTO person (person_id, year_of_birth) VALUES (?, ?)",
            (i, 1940 + (i % 80))  # 随机出生年 1940-2020
        )
    conn.commit()
    conn.close()

# Step 2: 调用函数 - 批量插入 node1 与 node2 数据库
if __name__ == "__main__":
    populate_fake_patients("data/node1.sqlite", 500)
    populate_fake_patients("data/node2.sqlite", 750)
    print("✅ 插入完成：node1=500人, node2=750人")
