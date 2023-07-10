from time import sleep

import psycopg2

_conn_with_task = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
_cursor = _conn_with_task.cursor()
"""查询最新的taskid并将其赋值给这个任务的id"""
_cursor.execute("SELECT value FROM keyvalues WHERE key = 'taskid'")
sign = _cursor.fetchone()[0]
sleep(1)