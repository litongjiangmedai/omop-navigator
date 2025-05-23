import sqlite3
import os
from app.utils import get_db_path

def run_sql_query(sql: str) -> str:
    db_path = get_db_path()
    if not os.path.exists(db_path):
        return "-- ⚠️ synthea_omop_with_concept.sqlite not found."
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchmany(5)
        columns = [desc[0] for desc in cur.description]
        result = [dict(zip(columns, row)) for row in rows]
        return str(result)
    finally:
        conn.close()
