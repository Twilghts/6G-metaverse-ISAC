import psycopg2

_conn_in_data_processing = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
_conn_in_data_processing.autocommit = True
_cursor_communicationdatadb = _conn_in_data_processing.cursor()
_cursor_communicationdatadb.execute("SELECT * FROM communicationdatadb order by id, delay")
datasets = _cursor_communicationdatadb.fetchall()
id = datasets[0][0]
delay = datasets[0][3]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay = datasets[index][3]
        datasets[index][3] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][3]
print("结束处理数据communicationdatadb")
_cursor_communicationdatadb.execute("DELETE FROM communicationdatadb")
print("结束删除原数据communicationdatadb")
insert_data = ("INSERT INTO communicationdatadb(id, timestamp, router_sign, delay,"
               " slice_sign, is_loss, task_id) VALUES (%s, %s, %s, %s, %s, %s, %s)")
_cursor_communicationdatadb.executemany(insert_data, datasets)
print("结束插入新数据communicationdatadb\n")
_cursor_communicationdatadb.close()

_cursor_communicationdatadb_comparison1 = _conn_in_data_processing.cursor()
_cursor_communicationdatadb_comparison1.execute("SELECT * FROM communicationdatadb_comparison order by id, delay")
datasets = _cursor_communicationdatadb_comparison1.fetchall()
id = datasets[0][0]
delay = datasets[0][3]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay = datasets[index][3]
        datasets[index][3] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][3]
print("结束处理数据communicationdatadb_comparison")
_cursor_communicationdatadb_comparison1.execute("DELETE FROM communicationdatadb_comparison")
print("结束删除原数据communicationdatadb_comparison")
insert_data = ("INSERT INTO communicationdatadb_comparison(id, timestamp, router_sign, delay,"
               " slice_sign, is_loss, task_id) VALUES (%s, %s, %s, %s, %s, %s, %s)")
_cursor_communicationdatadb_comparison1.executemany(insert_data, datasets)
print("结束插入新数据communicationdatadb_comparison\n")
_cursor_communicationdatadb_comparison1.close()

_cursor_communicationdatadb_comparison2 = _conn_in_data_processing.cursor()
_cursor_communicationdatadb_comparison2.execute("SELECT * FROM communicationdatadb_comparison2 order by id, delay")
datasets = _cursor_communicationdatadb_comparison2.fetchall()
id = datasets[0][0]
delay = datasets[0][3]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay = datasets[index][3]
        datasets[index][3] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][3]
print("结束处理数据communicationdatadb_comparison2")
_cursor_communicationdatadb_comparison2.execute("DELETE FROM communicationdatadb_comparison2")
print("结束删除原数据communicationdatadb_comparison2")
insert_data = ("INSERT INTO communicationdatadb_comparison2(id, timestamp, router_sign, delay,"
               " slice_sign, is_loss, task_id) VALUES (%s, %s, %s, %s, %s, %s, %s)")
_cursor_communicationdatadb_comparison2.executemany(insert_data, datasets)
print("结束插入新数据communicationdatadb_comparison2\n")
_cursor_communicationdatadb_comparison2.close()

_cursor_sensordatadb = _conn_in_data_processing.cursor()
_cursor_sensordatadb.execute("SELECT * FROM sensordatadb order by id, delay")
datasets = _cursor_sensordatadb.fetchall()
id = datasets[0][0]
delay = datasets[0][5]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay = datasets[index][5]
        datasets[index][5] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][5]
print("结束处理数据sensordatadb")
_cursor_sensordatadb.execute("DELETE FROM sensordatadb")
print("结束删除原数据sensordatadb")
insert_data = ("INSERT INTO sensordatadb(id, time, router_id, slice_id, is_loss, delay,"
               " specific_type, task_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
_cursor_sensordatadb.executemany(insert_data, datasets)
print("结束插入新数据sensordatadb\n")
_cursor_sensordatadb.close()

_cursor_sensordatadb_comparison = _conn_in_data_processing.cursor()
_cursor_sensordatadb_comparison.execute("SELECT * FROM sensordatadb_comparison order by id, delay")
datasets = _cursor_sensordatadb_comparison.fetchall()
id = datasets[0][0]
delay = datasets[0][5]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay = datasets[index][5]
        datasets[index][5] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][5]
print("结束处理数据sensordatadb_comparison")
_cursor_sensordatadb_comparison.execute("DELETE FROM sensordatadb_comparison")
print("结束删除原数据sensordatadb_comparison")
insert_data = ("INSERT INTO sensordatadb_comparison(id, time, router_id, slice_id, is_loss, delay,"
               " specific_type, task_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
_cursor_sensordatadb_comparison.executemany(insert_data, datasets)
print("结束插入新数据sensordatadb_comparison\n")
_cursor_sensordatadb_comparison.close()

_cursor_sensordatadb_comparison2 = _conn_in_data_processing.cursor()
_cursor_sensordatadb_comparison2.execute("SELECT * FROM sensordatadb_comparison2 order by id, delay")
datasets = _cursor_sensordatadb_comparison2.fetchall()
id = datasets[0][0]
delay = datasets[0][6]
for index in range(len(datasets)):
    datasets[index] = list(datasets[index])
for index in range(1, len(datasets)):
    if datasets[index][0] == id:
        tem_delay: float = datasets[index][6]
        datasets[index][6] -= delay
        delay = tem_delay
    else:
        id = datasets[index][0]
        delay = datasets[index][6]
print("结束处理数据sensordatadb_comparison2")
_cursor_sensordatadb_comparison2.execute("DELETE FROM sensordatadb_comparison2")
print("结束删除原数据sensordatadb_comparison2")
insert_data = ("INSERT INTO sensordatadb_comparison2(id, time, router_id, slice_id, is_loss, task_id, delay,"
               " specific_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
_cursor_sensordatadb_comparison2.executemany(insert_data, datasets)
print("结束插入新数据sensordatadb_comparison2\n")
_cursor_sensordatadb_comparison2.close()
_conn_in_data_processing.close()
print("结束程序运行")
