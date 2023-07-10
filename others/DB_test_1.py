import time

import psycopg2

_conn_with_task = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
_cursor = _conn_with_task.cursor()
_sql_for_task = 'INSERT INTO test (id)  ' \
                'VALUES (%s)'

start_time = time.perf_counter()
for i in range(10):
    _cursor.execute(_sql_for_task, (i, ))
print(time.perf_counter() - start_time)

start_time = time.perf_counter()
values = []
for i in range(10, 20):
    values.append((i, ))
_cursor.executemany(_sql_for_task, values)
print(time.perf_counter() - start_time)

