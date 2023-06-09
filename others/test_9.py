import psycopg2

_conn_with_task = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
_cursor = _conn_with_task.cursor()
_sql_for_task = 'INSERT INTO action_area ("0_0", "0_1", "0_2", "1_0", "1_1", "1_2", "2_0", "2_1", "2_2")  ' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

matrix = [[[0.2, 0.7, 0.1], [0.2, 0.4, 0.4], [0.2, 0.3, 0.5]],
          [[0.7, 0.1, 0.2], [0.2, 0.6, 0.2], [0.2, 0.4, 0.4]],
          [[0.1, 0.4, 0.5], [0.1, 0.1, 0.8], [0.1, 0.7, 0.2]],
          [[0.1, 0.2, 0.7], [0.3, 0.1, 0.6], [0.5, 0.2, 0.3]],
          [[0.3, 0.5, 0.2], [0.1, 0.4, 0.5], [0.7, 0.1, 0.2]],
          [[0.6, 0.2, 0.2], [0.7, 0.1, 0.2], [0.4, 0.3, 0.3]],
          [[0.3, 0.6, 0.1], [0.1, 0.6, 0.3], [0.4, 0.3, 0.3]],
          [[0.1, 0.1, 0.8], [0.5, 0.3, 0.2], [0.2, 0.7, 0.1]],
          [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.6, 0.2, 0.2]],
          [[0.1, 0.3, 0.6], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
          [[0.4, 0.1, 0.5], [0.6, 0.1, 0.3], [0.2, 0.3, 0.5]],
          [[0.6, 0.1, 0.3], [0.4, 0.4, 0.2], [0.3, 0.1, 0.6]],
          [[0.4, 0.4, 0.2], [0.3, 0.6, 0.1], [0.4, 0.3, 0.3]],
          [[0.1, 0.3, 0.6], [0.4, 0.3, 0.3], [0.3, 0.4, 0.3]],
          [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
          [[0.1, 0.3, 0.6], [0.7, 0.1, 0.2], [0.5, 0.4, 0.1]],
          [[0.1, 0.6, 0.3], [0.6, 0.1, 0.3], [0.5, 0.3, 0.2]],
          [[0.3, 0.4, 0.3], [0.2, 0.4, 0.4], [0.2, 0.1, 0.7]],
          [[0.2, 0.4, 0.4], [0.3, 0.4, 0.3], [0.2, 0.6, 0.2]],
          [[0.4, 0.2, 0.4], [0.7, 0.1, 0.2], [0.3, 0.5, 0.2]],
          [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.3, 0.5, 0.2]],
          [[0.3, 0.3, 0.4], [0.6, 0.2, 0.2], [0.1, 0.1, 0.8]],
          [[0.4, 0.2, 0.4], [0.2, 0.5, 0.3], [0.2, 0.6, 0.2]],
          [[0.3, 0.6, 0.1], [0.1, 0.3, 0.6], [0.1, 0.2, 0.7]],
          [[0.1, 0.2, 0.7], [0.8, 0.1, 0.1], [0.2, 0.1, 0.7]],
          [[0.1, 0.1, 0.8], [0.3, 0.5, 0.2], [0.3, 0.4, 0.3]],
          [[0.2, 0.7, 0.1], [0.4, 0.5, 0.1], [0.1, 0.4, 0.5]],
          [[0.6, 0.1, 0.3], [0.1, 0.7, 0.2], [0.8, 0.1, 0.1]],
          [[0.2, 0.6, 0.2], [0.2, 0.1, 0.7], [0.4, 0.1, 0.5]],
          [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.1, 0.2, 0.7]],
          [[0.4, 0.3, 0.3], [0.6, 0.3, 0.1], [0.1, 0.3, 0.6]],
          [[0.1, 0.1, 0.8], [0.2, 0.1, 0.7], [0.3, 0.1, 0.6]],
          [[0.1, 0.8, 0.1], [0.5, 0.2, 0.3], [0.3, 0.5, 0.2]],
          [[0.3, 0.2, 0.5], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
          [[0.1, 0.4, 0.5], [0.5, 0.3, 0.2], [0.5, 0.1, 0.4]],
          [[0.3, 0.1, 0.6], [0.5, 0.4, 0.1], [0.1, 0.5, 0.4]],
          [[0.7, 0.2, 0.1], [0.2, 0.1, 0.7], [0.1, 0.1, 0.8]],
          [[0.2, 0.6, 0.2], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
          [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]],
          [[0.4, 0.4, 0.2], [0.5, 0.2, 0.3], [0.1, 0.6, 0.3]],
          [[0.3, 0.3, 0.4], [0.5, 0.1, 0.4], [0.6, 0.1, 0.3]],
          [[0.2, 0.4, 0.4], [0.1, 0.5, 0.4], [0.2, 0.1, 0.7]],
          [[0.3, 0.1, 0.6], [0.1, 0.7, 0.2], [0.4, 0.2, 0.4]],
          [[0.3, 0.3, 0.4], [0.1, 0.3, 0.6], [0.3, 0.2, 0.5]],
          [[0.1, 0.6, 0.3], [0.6, 0.3, 0.1], [0.3, 0.1, 0.6]],
          [[0.3, 0.5, 0.2], [0.4, 0.5, 0.1], [0.6, 0.3, 0.1]],
          [[0.4, 0.3, 0.3], [0.1, 0.4, 0.5], [0.1, 0.6, 0.3]],
          [[0.5, 0.4, 0.1], [0.2, 0.2, 0.6], [0.3, 0.2, 0.5]],
          [[0.3, 0.6, 0.1], [0.4, 0.3, 0.3], [0.5, 0.2, 0.3]],
          [[0.3, 0.5, 0.2], [0.2, 0.2, 0.6], [0.4, 0.2, 0.4]],
          [[0.8, 0.1, 0.1], [0.1, 0.6, 0.3], [0.1, 0.1, 0.8]],
          [[0.1, 0.8, 0.1], [0.1, 0.5, 0.4], [0.3, 0.6, 0.1]],
          [[0.1, 0.2, 0.7], [0.2, 0.7, 0.1], [0.2, 0.6, 0.2]],
          [[0.3, 0.5, 0.2], [0.4, 0.1, 0.5], [0.4, 0.5, 0.1]],
          [[0.3, 0.6, 0.1], [0.5, 0.4, 0.1], [0.4, 0.1, 0.5]],
          [[0.4, 0.4, 0.2], [0.3, 0.1, 0.6], [0.3, 0.4, 0.3]],
          [[0.1, 0.7, 0.2], [0.3, 0.4, 0.3], [0.5, 0.1, 0.4]],
          [[0.6, 0.1, 0.3], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1]],
          [[0.8, 0.1, 0.1], [0.1, 0.3, 0.6], [0.2, 0.5, 0.3]],
          [[0.1, 0.2, 0.7], [0.3, 0.4, 0.3], [0.1, 0.8, 0.1]],
          [[0.2, 0.4, 0.4], [0.1, 0.7, 0.2], [0.1, 0.5, 0.4]],
          [[0.4, 0.5, 0.1], [0.5, 0.3, 0.2], [0.1, 0.2, 0.7]],
          [[0.3, 0.5, 0.2], [0.1, 0.3, 0.6], [0.5, 0.4, 0.1]],
          [[0.8, 0.1, 0.1], [0.4, 0.4, 0.2], [0.5, 0.4, 0.1]],
          [[0.7, 0.2, 0.1], [0.8, 0.1, 0.1], [0.5, 0.3, 0.2]],
          [[0.7, 0.1, 0.2], [0.2, 0.1, 0.7], [0.6, 0.1, 0.3]],
          [[0.3, 0.6, 0.1], [0.2, 0.4, 0.4], [0.1, 0.2, 0.7]],
          [[0.2, 0.3, 0.5], [0.2, 0.5, 0.3], [0.1, 0.2, 0.7]],
          [[0.2, 0.4, 0.4], [0.5, 0.4, 0.1], [0.2, 0.7, 0.1]],
          [[0.7, 0.1, 0.2], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
          [[0.3, 0.1, 0.6], [0.2, 0.2, 0.6], [0.1, 0.8, 0.1]],
          [[0.2, 0.4, 0.4], [0.3, 0.4, 0.3], [0.2, 0.7, 0.1]],
          [[0.1, 0.8, 0.1], [0.7, 0.2, 0.1], [0.2, 0.4, 0.4]],
          [[0.5, 0.2, 0.3], [0.2, 0.3, 0.5], [0.1, 0.5, 0.4]],
          [[0.2, 0.1, 0.7], [0.3, 0.5, 0.2], [0.2, 0.5, 0.3]],
          [[0.1, 0.6, 0.3], [0.6, 0.1, 0.3], [0.1, 0.7, 0.2]],
          [[0.3, 0.3, 0.4], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
          [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.2, 0.5, 0.3]],
          [[0.4, 0.4, 0.2], [0.1, 0.6, 0.3], [0.6, 0.2, 0.2]],
          [[0.4, 0.2, 0.4], [0.1, 0.3, 0.6], [0.2, 0.7, 0.1]],
          [[0.2, 0.1, 0.7], [0.2, 0.3, 0.5], [0.4, 0.3, 0.3]],
          [[0.1, 0.1, 0.8], [0.1, 0.3, 0.6], [0.6, 0.2, 0.2]],
          [[0.5, 0.4, 0.1], [0.2, 0.5, 0.3], [0.2, 0.7, 0.1]],
          [[0.2, 0.5, 0.3], [0.5, 0.2, 0.3], [0.1, 0.6, 0.3]],
          [[0.2, 0.5, 0.3], [0.3, 0.6, 0.1], [0.7, 0.2, 0.1]],
          [[0.5, 0.4, 0.1], [0.2, 0.1, 0.7], [0.4, 0.4, 0.2]],
          [[0.1, 0.1, 0.8], [0.4, 0.2, 0.4], [0.1, 0.4, 0.5]],
          [[0.1, 0.2, 0.7], [0.6, 0.1, 0.3], [0.1, 0.5, 0.4]],
          [[0.2, 0.2, 0.6], [0.4, 0.3, 0.3], [0.1, 0.4, 0.5]],
          [[0.2, 0.4, 0.4], [0.3, 0.6, 0.1], [0.1, 0.2, 0.7]],
          [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.7, 0.2, 0.1]],
          [[0.8, 0.1, 0.1], [0.1, 0.1, 0.8], [0.1, 0.5, 0.4]],
          [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.1, 0.5, 0.4]],
          [[0.1, 0.1, 0.8], [0.2, 0.1, 0.7], [0.6, 0.2, 0.2]],
          [[0.6, 0.1, 0.3], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
          [[0.1, 0.7, 0.2], [0.3, 0.6, 0.1], [0.1, 0.4, 0.5]],
          [[0.2, 0.5, 0.3], [0.3, 0.1, 0.6], [0.4, 0.1, 0.5]],
          [[0.8, 0.1, 0.1], [0.3, 0.4, 0.3], [0.2, 0.1, 0.7]],
          [[0.1, 0.7, 0.2], [0.3, 0.4, 0.3], [0.3, 0.2, 0.5]],
          [[0.1, 0.4, 0.5], [0.2, 0.6, 0.2], [0.1, 0.5, 0.4]],
          [[0.1, 0.1, 0.8], [0.6, 0.2, 0.2], [0.1, 0.3, 0.6]],
          [[0.5, 0.1, 0.4], [0.1, 0.6, 0.3], [0.6, 0.2, 0.2]],
          [[0.8, 0.1, 0.1], [0.5, 0.4, 0.1], [0.7, 0.2, 0.1]],
          [[0.8, 0.1, 0.1], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
          [[0.1, 0.2, 0.7], [0.5, 0.1, 0.4], [0.5, 0.2, 0.3]],
          [[0.5, 0.2, 0.3], [0.6, 0.2, 0.2], [0.2, 0.3, 0.5]],
          [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.3, 0.6, 0.1]],
          [[0.6, 0.3, 0.1], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
          [[0.2, 0.1, 0.7], [0.1, 0.1, 0.8], [0.2, 0.3, 0.5]],
          [[0.2, 0.4, 0.4], [0.2, 0.1, 0.7], [0.3, 0.3, 0.4]],
          [[0.4, 0.5, 0.1], [0.6, 0.1, 0.3], [0.8, 0.1, 0.1]],
          [[0.3, 0.6, 0.1], [0.1, 0.4, 0.5], [0.4, 0.2, 0.4]],
          [[0.6, 0.1, 0.3], [0.8, 0.1, 0.1], [0.2, 0.1, 0.7]],
          [[0.3, 0.6, 0.1], [0.3, 0.2, 0.5], [0.1, 0.1, 0.8]],
          [[0.6, 0.2, 0.2], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3]],
          [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.1, 0.5, 0.4]],
          [[0.6, 0.2, 0.2], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
          [[0.2, 0.6, 0.2], [0.3, 0.1, 0.6], [0.1, 0.5, 0.4]],
          [[0.5, 0.4, 0.1], [0.1, 0.2, 0.7], [0.4, 0.1, 0.5]],
          [[0.2, 0.6, 0.2], [0.5, 0.4, 0.1], [0.4, 0.5, 0.1]],
          [[0.5, 0.4, 0.1], [0.6, 0.1, 0.3], [0.3, 0.4, 0.3]],
          [[0.1, 0.8, 0.1], [0.5, 0.3, 0.2], [0.1, 0.6, 0.3]],
          [[0.7, 0.2, 0.1], [0.6, 0.3, 0.1], [0.5, 0.2, 0.3]],
          [[0.4, 0.5, 0.1], [0.3, 0.4, 0.3], [0.1, 0.6, 0.3]],
          [[0.3, 0.3, 0.4], [0.6, 0.3, 0.1], [0.2, 0.1, 0.7]],
          [[0.2, 0.7, 0.1], [0.1, 0.1, 0.8], [0.5, 0.4, 0.1]],
          [[0.2, 0.6, 0.2], [0.4, 0.1, 0.5], [0.7, 0.2, 0.1]],
          [[0.1, 0.1, 0.8], [0.1, 0.3, 0.6], [0.3, 0.3, 0.4]],
          [[0.5, 0.2, 0.3], [0.1, 0.8, 0.1], [0.3, 0.1, 0.6]],
          [[0.2, 0.6, 0.2], [0.5, 0.4, 0.1], [0.6, 0.2, 0.2]],
          [[0.3, 0.4, 0.3], [0.1, 0.8, 0.1], [0.1, 0.2, 0.7]],
          [[0.4, 0.3, 0.3], [0.3, 0.5, 0.2], [0.2, 0.1, 0.7]],
          [[0.1, 0.4, 0.5], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
          [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.2, 0.7, 0.1]],
          [[0.7, 0.1, 0.2], [0.3, 0.6, 0.1], [0.1, 0.8, 0.1]],
          [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.1, 0.8, 0.1]],
          [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.1, 0.7, 0.2]],
          [[0.5, 0.1, 0.4], [0.4, 0.3, 0.3], [0.2, 0.3, 0.5]],
          [[0.7, 0.1, 0.2], [0.8, 0.1, 0.1], [0.6, 0.3, 0.1]],
          [[0.7, 0.2, 0.1], [0.4, 0.1, 0.5], [0.2, 0.7, 0.1]],
          [[0.4, 0.4, 0.2], [0.2, 0.3, 0.5], [0.2, 0.4, 0.4]],
          [[0.1, 0.6, 0.3], [0.1, 0.1, 0.8], [0.3, 0.2, 0.5]],
          [[0.1, 0.4, 0.5], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
          [[0.2, 0.1, 0.7], [0.4, 0.1, 0.5], [0.7, 0.2, 0.1]],
          [[0.4, 0.2, 0.4], [0.1, 0.6, 0.3], [0.2, 0.6, 0.2]],
          [[0.1, 0.1, 0.8], [0.6, 0.3, 0.1], [0.2, 0.5, 0.3]],
          [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.3, 0.6, 0.1]],
          [[0.5, 0.2, 0.3], [0.4, 0.3, 0.3], [0.1, 0.2, 0.7]],
          [[0.1, 0.4, 0.5], [0.7, 0.2, 0.1], [0.3, 0.6, 0.1]],
          [[0.4, 0.2, 0.4], [0.3, 0.5, 0.2], [0.7, 0.2, 0.1]],
          [[0.3, 0.4, 0.3], [0.2, 0.6, 0.2], [0.1, 0.3, 0.6]],
          [[0.4, 0.3, 0.3], [0.4, 0.1, 0.5], [0.8, 0.1, 0.1]],
          [[0.1, 0.2, 0.7], [0.5, 0.1, 0.4], [0.2, 0.7, 0.1]],
          [[0.1, 0.5, 0.4], [0.3, 0.4, 0.3], [0.3, 0.6, 0.1]],
          [[0.1, 0.7, 0.2], [0.2, 0.7, 0.1], [0.1, 0.5, 0.4]],
          [[0.3, 0.5, 0.2], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
          [[0.3, 0.3, 0.4], [0.3, 0.1, 0.6], [0.4, 0.1, 0.5]],
          [[0.4, 0.3, 0.3], [0.2, 0.1, 0.7], [0.5, 0.4, 0.1]],
          [[0.2, 0.1, 0.7], [0.6, 0.2, 0.2], [0.2, 0.4, 0.4]],
          [[0.2, 0.3, 0.5], [0.1, 0.6, 0.3], [0.7, 0.1, 0.2]],
          [[0.2, 0.5, 0.3], [0.1, 0.2, 0.7], [0.3, 0.5, 0.2]],
          [[0.1, 0.3, 0.6], [0.6, 0.2, 0.2], [0.7, 0.2, 0.1]],
          [[0.3, 0.3, 0.4], [0.6, 0.1, 0.3], [0.4, 0.2, 0.4]],
          [[0.4, 0.1, 0.5], [0.2, 0.1, 0.7], [0.3, 0.1, 0.6]],
          [[0.1, 0.3, 0.6], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
          [[0.2, 0.5, 0.3], [0.2, 0.4, 0.4], [0.4, 0.3, 0.3]],
          [[0.7, 0.2, 0.1], [0.6, 0.2, 0.2], [0.2, 0.5, 0.3]],
          [[0.4, 0.4, 0.2], [0.4, 0.1, 0.5], [0.4, 0.5, 0.1]],
          [[0.3, 0.5, 0.2], [0.5, 0.3, 0.2], [0.5, 0.1, 0.4]],
          [[0.2, 0.3, 0.5], [0.7, 0.1, 0.2], [0.5, 0.4, 0.1]],
          [[0.7, 0.2, 0.1], [0.1, 0.4, 0.5], [0.3, 0.4, 0.3]],
          [[0.4, 0.2, 0.4], [0.7, 0.1, 0.2], [0.1, 0.1, 0.8]],
          [[0.8, 0.1, 0.1], [0.4, 0.5, 0.1], [0.2, 0.5, 0.3]],
          [[0.7, 0.2, 0.1], [0.2, 0.2, 0.6], [0.3, 0.1, 0.6]],
          [[0.3, 0.6, 0.1], [0.6, 0.3, 0.1], [0.2, 0.2, 0.6]],
          [[0.2, 0.7, 0.1], [0.2, 0.2, 0.6], [0.4, 0.2, 0.4]],
          [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.6, 0.2, 0.2]],
          [[0.6, 0.3, 0.1], [0.8, 0.1, 0.1], [0.1, 0.7, 0.2]],
          [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.1, 0.6, 0.3]],
          [[0.2, 0.2, 0.6], [0.6, 0.1, 0.3], [0.2, 0.4, 0.4]],
          [[0.6, 0.2, 0.2], [0.4, 0.4, 0.2], [0.5, 0.1, 0.4]],
          [[0.8, 0.1, 0.1], [0.2, 0.5, 0.3], [0.3, 0.6, 0.1]],
          [[0.1, 0.8, 0.1], [0.6, 0.3, 0.1], [0.4, 0.2, 0.4]],
          [[0.2, 0.5, 0.3], [0.3, 0.3, 0.4], [0.5, 0.4, 0.1]],
          [[0.4, 0.3, 0.3], [0.3, 0.6, 0.1], [0.2, 0.6, 0.2]],
          [[0.4, 0.5, 0.1], [0.6, 0.1, 0.3], [0.3, 0.4, 0.3]],
          [[0.3, 0.6, 0.1], [0.7, 0.1, 0.2], [0.2, 0.2, 0.6]],
          [[0.1, 0.5, 0.4], [0.4, 0.5, 0.1], [0.1, 0.3, 0.6]],
          [[0.5, 0.2, 0.3], [0.2, 0.5, 0.3], [0.1, 0.3, 0.6]],
          [[0.7, 0.1, 0.2], [0.7, 0.2, 0.1], [0.2, 0.1, 0.7]],
          [[0.2, 0.7, 0.1], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
          [[0.3, 0.3, 0.4], [0.4, 0.5, 0.1], [0.2, 0.7, 0.1]],
          [[0.3, 0.1, 0.6], [0.7, 0.1, 0.2], [0.2, 0.4, 0.4]],
          [[0.3, 0.4, 0.3], [0.4, 0.1, 0.5], [0.8, 0.1, 0.1]],
          [[0.5, 0.3, 0.2], [0.6, 0.3, 0.1], [0.3, 0.1, 0.6]],
          [[0.1, 0.7, 0.2], [0.7, 0.2, 0.1], [0.6, 0.2, 0.2]],
          [[0.2, 0.7, 0.1], [0.6, 0.1, 0.3], [0.6, 0.3, 0.1]],
          [[0.5, 0.4, 0.1], [0.5, 0.2, 0.3], [0.1, 0.1, 0.8]],
          [[0.2, 0.2, 0.6], [0.4, 0.2, 0.4], [0.3, 0.1, 0.6]],
          [[0.7, 0.1, 0.2], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
          [[0.1, 0.5, 0.4], [0.1, 0.3, 0.6], [0.3, 0.5, 0.2]],
          [[0.8, 0.1, 0.1], [0.5, 0.4, 0.1], [0.4, 0.4, 0.2]],
          [[0.8, 0.1, 0.1], [0.6, 0.1, 0.3], [0.5, 0.3, 0.2]],
          [[0.4, 0.3, 0.3], [0.2, 0.4, 0.4], [0.1, 0.6, 0.3]],
          [[0.2, 0.5, 0.3], [0.3, 0.2, 0.5], [0.1, 0.4, 0.5]],
          [[0.1, 0.8, 0.1], [0.1, 0.7, 0.2], [0.1, 0.6, 0.3]],
          [[0.2, 0.5, 0.3], [0.4, 0.1, 0.5], [0.2, 0.2, 0.6]],
          [[0.4, 0.2, 0.4], [0.6, 0.1, 0.3], [0.7, 0.1, 0.2]],
          [[0.5, 0.3, 0.2], [0.3, 0.1, 0.6], [0.6, 0.3, 0.1]],
          [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.2, 0.7, 0.1]],
          [[0.4, 0.2, 0.4], [0.3, 0.2, 0.5], [0.8, 0.1, 0.1]],
          [[0.4, 0.3, 0.3], [0.1, 0.4, 0.5], [0.4, 0.1, 0.5]],
          [[0.4, 0.4, 0.2], [0.7, 0.2, 0.1], [0.4, 0.1, 0.5]],
          [[0.1, 0.8, 0.1], [0.3, 0.4, 0.3], [0.5, 0.4, 0.1]],
          [[0.3, 0.3, 0.4], [0.1, 0.3, 0.6], [0.7, 0.1, 0.2]],
          [[0.4, 0.1, 0.5], [0.3, 0.3, 0.4], [0.2, 0.6, 0.2]],
          [[0.6, 0.2, 0.2], [0.1, 0.1, 0.8], [0.2, 0.3, 0.5]],
          [[0.2, 0.1, 0.7], [0.3, 0.1, 0.6], [0.7, 0.1, 0.2]],
          [[0.2, 0.3, 0.5], [0.6, 0.2, 0.2], [0.2, 0.1, 0.7]],
          [[0.2, 0.1, 0.7], [0.2, 0.7, 0.1], [0.2, 0.5, 0.3]],
          [[0.6, 0.2, 0.2], [0.4, 0.5, 0.1], [0.2, 0.6, 0.2]],
          [[0.5, 0.1, 0.4], [0.1, 0.7, 0.2], [0.3, 0.6, 0.1]],
          [[0.1, 0.6, 0.3], [0.2, 0.1, 0.7], [0.2, 0.7, 0.1]],
          [[0.1, 0.6, 0.3], [0.5, 0.4, 0.1], [0.7, 0.2, 0.1]],
          [[0.4, 0.5, 0.1], [0.6, 0.2, 0.2], [0.6, 0.1, 0.3]],
          [[0.2, 0.5, 0.3], [0.4, 0.4, 0.2], [0.5, 0.3, 0.2]],
          [[0.3, 0.1, 0.6], [0.3, 0.5, 0.2], [0.4, 0.1, 0.5]],
          [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.2, 0.1, 0.7]],
          [[0.3, 0.2, 0.5], [0.4, 0.4, 0.2], [0.5, 0.1, 0.4]],
          [[0.3, 0.2, 0.5], [0.1, 0.5, 0.4], [0.8, 0.1, 0.1]],
          [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.1, 0.6]],
          [[0.1, 0.6, 0.3], [0.5, 0.2, 0.3], [0.8, 0.1, 0.1]],
          [[0.4, 0.3, 0.3], [0.5, 0.1, 0.4], [0.2, 0.7, 0.1]],
          [[0.5, 0.3, 0.2], [0.3, 0.4, 0.3], [0.8, 0.1, 0.1]],
          [[0.1, 0.3, 0.6], [0.1, 0.8, 0.1], [0.1, 0.7, 0.2]],
          [[0.4, 0.5, 0.1], [0.1, 0.4, 0.5], [0.2, 0.4, 0.4]],
          [[0.3, 0.1, 0.6], [0.5, 0.4, 0.1], [0.4, 0.3, 0.3]],
          [[0.7, 0.2, 0.1], [0.2, 0.6, 0.2], [0.3, 0.2, 0.5]],
          [[0.2, 0.3, 0.5], [0.5, 0.4, 0.1], [0.6, 0.1, 0.3]],
          [[0.2, 0.7, 0.1], [0.1, 0.6, 0.3], [0.5, 0.2, 0.3]],
          [[0.1, 0.8, 0.1], [0.4, 0.4, 0.2], [0.7, 0.1, 0.2]],
          [[0.2, 0.5, 0.3], [0.6, 0.3, 0.1], [0.1, 0.2, 0.7]],
          [[0.1, 0.2, 0.7], [0.4, 0.5, 0.1], [0.5, 0.2, 0.3]],
          [[0.6, 0.1, 0.3], [0.1, 0.4, 0.5], [0.1, 0.8, 0.1]],
          [[0.1, 0.8, 0.1], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
          [[0.4, 0.3, 0.3], [0.2, 0.2, 0.6], [0.1, 0.8, 0.1]],
          [[0.3, 0.4, 0.3], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
          [[0.4, 0.5, 0.1], [0.4, 0.4, 0.2], [0.2, 0.5, 0.3]],
          [[0.4, 0.1, 0.5], [0.4, 0.4, 0.2], [0.1, 0.7, 0.2]],
          [[0.6, 0.1, 0.3], [0.5, 0.3, 0.2], [0.1, 0.6, 0.3]],
          [[0.5, 0.3, 0.2], [0.2, 0.7, 0.1], [0.3, 0.6, 0.1]],
          [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.4, 0.4, 0.2]],
          [[0.1, 0.3, 0.6], [0.4, 0.3, 0.3], [0.1, 0.7, 0.2]],
          [[0.4, 0.4, 0.2], [0.2, 0.1, 0.7], [0.5, 0.4, 0.1]],
          [[0.2, 0.1, 0.7], [0.7, 0.2, 0.1], [0.5, 0.2, 0.3]],
          [[0.5, 0.3, 0.2], [0.5, 0.4, 0.1], [0.7, 0.1, 0.2]],
          [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6]],
          [[0.2, 0.2, 0.6], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1]],
          [[0.1, 0.6, 0.3], [0.2, 0.3, 0.5], [0.2, 0.1, 0.7]],
          [[0.2, 0.6, 0.2], [0.1, 0.1, 0.8], [0.1, 0.4, 0.5]],
          [[0.5, 0.2, 0.3], [0.2, 0.1, 0.7], [0.4, 0.4, 0.2]],
          [[0.1, 0.5, 0.4], [0.4, 0.5, 0.1], [0.1, 0.3, 0.6]],
          [[0.5, 0.3, 0.2], [0.4, 0.2, 0.4], [0.7, 0.2, 0.1]],
          [[0.1, 0.1, 0.8], [0.2, 0.7, 0.1], [0.3, 0.4, 0.3]],
          [[0.4, 0.2, 0.4], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
          [[0.4, 0.2, 0.4], [0.3, 0.3, 0.4], [0.1, 0.5, 0.4]],
          [[0.2, 0.6, 0.2], [0.2, 0.4, 0.4], [0.3, 0.5, 0.2]],
          [[0.3, 0.1, 0.6], [0.3, 0.2, 0.5], [0.1, 0.4, 0.5]],
          [[0.2, 0.3, 0.5], [0.3, 0.2, 0.5], [0.1, 0.6, 0.3]],
          [[0.2, 0.5, 0.3], [0.2, 0.1, 0.7], [0.7, 0.1, 0.2]],
          [[0.6, 0.1, 0.3], [0.6, 0.2, 0.2], [0.5, 0.4, 0.1]],
          [[0.3, 0.4, 0.3], [0.6, 0.1, 0.3], [0.1, 0.7, 0.2]],
          [[0.3, 0.5, 0.2], [0.6, 0.2, 0.2], [0.2, 0.3, 0.5]],
          [[0.2, 0.2, 0.6], [0.4, 0.3, 0.3], [0.2, 0.4, 0.4]],
          [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.5, 0.4, 0.1]],
          [[0.2, 0.5, 0.3], [0.7, 0.2, 0.1], [0.3, 0.1, 0.6]],
          [[0.1, 0.8, 0.1], [0.1, 0.1, 0.8], [0.3, 0.1, 0.6]],
          [[0.1, 0.6, 0.3], [0.2, 0.6, 0.2], [0.2, 0.2, 0.6]],
          [[0.4, 0.5, 0.1], [0.7, 0.2, 0.1], [0.4, 0.3, 0.3]],
          [[0.3, 0.5, 0.2], [0.2, 0.6, 0.2], [0.3, 0.4, 0.3]],
          [[0.4, 0.1, 0.5], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
          [[0.2, 0.3, 0.5], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
          [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.5, 0.1, 0.4]],
          [[0.1, 0.8, 0.1], [0.4, 0.1, 0.5], [0.1, 0.4, 0.5]],
          [[0.2, 0.4, 0.4], [0.4, 0.2, 0.4], [0.5, 0.2, 0.3]],
          [[0.5, 0.4, 0.1], [0.4, 0.1, 0.5], [0.3, 0.4, 0.3]],
          [[0.4, 0.2, 0.4], [0.3, 0.4, 0.3], [0.3, 0.6, 0.1]],
          [[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.6, 0.2]],
          [[0.1, 0.5, 0.4], [0.4, 0.1, 0.5], [0.1, 0.4, 0.5]],
          [[0.5, 0.2, 0.3], [0.2, 0.7, 0.1], [0.3, 0.2, 0.5]],
          [[0.8, 0.1, 0.1], [0.2, 0.5, 0.3], [0.1, 0.2, 0.7]],
          [[0.2, 0.7, 0.1], [0.1, 0.4, 0.5], [0.7, 0.1, 0.2]],
          [[0.7, 0.1, 0.2], [0.2, 0.6, 0.2], [0.3, 0.3, 0.4]],
          [[0.5, 0.2, 0.3], [0.4, 0.4, 0.2], [0.6, 0.3, 0.1]],
          [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.4, 0.1, 0.5]],
          [[0.2, 0.3, 0.5], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]],
          [[0.2, 0.2, 0.6], [0.6, 0.3, 0.1], [0.1, 0.2, 0.7]],
          [[0.3, 0.5, 0.2], [0.1, 0.7, 0.2], [0.4, 0.2, 0.4]],
          [[0.2, 0.4, 0.4], [0.6, 0.2, 0.2], [0.4, 0.3, 0.3]],
          [[0.2, 0.1, 0.7], [0.2, 0.3, 0.5], [0.3, 0.2, 0.5]],
          [[0.3, 0.1, 0.6], [0.2, 0.3, 0.5], [0.5, 0.3, 0.2]],
          [[0.3, 0.3, 0.4], [0.3, 0.4, 0.3], [0.5, 0.2, 0.3]],
          [[0.5, 0.3, 0.2], [0.1, 0.3, 0.6], [0.3, 0.1, 0.6]],
          [[0.4, 0.3, 0.3], [0.6, 0.3, 0.1], [0.6, 0.1, 0.3]],
          [[0.8, 0.1, 0.1], [0.1, 0.1, 0.8], [0.3, 0.2, 0.5]],
          [[0.2, 0.5, 0.3], [0.1, 0.6, 0.3], [0.3, 0.3, 0.4]],
          [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.1, 0.5, 0.4]],
          [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.4, 0.4, 0.2]],
          [[0.5, 0.4, 0.1], [0.5, 0.1, 0.4], [0.7, 0.1, 0.2]],
          [[0.5, 0.4, 0.1], [0.4, 0.2, 0.4], [0.4, 0.3, 0.3]],
          [[0.1, 0.6, 0.3], [0.4, 0.1, 0.5], [0.4, 0.2, 0.4]],
          [[0.1, 0.7, 0.2], [0.3, 0.6, 0.1], [0.1, 0.5, 0.4]],
          [[0.2, 0.5, 0.3], [0.7, 0.2, 0.1], [0.6, 0.1, 0.3]],
          [[0.3, 0.3, 0.4], [0.4, 0.2, 0.4], [0.1, 0.7, 0.2]],
          [[0.7, 0.1, 0.2], [0.3, 0.4, 0.3], [0.3, 0.3, 0.4]],
          [[0.2, 0.4, 0.4], [0.1, 0.2, 0.7], [0.1, 0.7, 0.2]],
          [[0.3, 0.6, 0.1], [0.2, 0.7, 0.1], [0.2, 0.2, 0.6]],
          [[0.4, 0.1, 0.5], [0.8, 0.1, 0.1], [0.6, 0.1, 0.3]],
          [[0.6, 0.2, 0.2], [0.4, 0.4, 0.2], [0.3, 0.3, 0.4]],
          [[0.1, 0.3, 0.6], [0.1, 0.2, 0.7], [0.6, 0.1, 0.3]],
          [[0.1, 0.5, 0.4], [0.2, 0.3, 0.5], [0.1, 0.6, 0.3]],
          [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.4, 0.5, 0.1]],
          [[0.5, 0.3, 0.2], [0.1, 0.1, 0.8], [0.4, 0.3, 0.3]],
          [[0.2, 0.1, 0.7], [0.4, 0.4, 0.2], [0.6, 0.1, 0.3]],
          [[0.5, 0.1, 0.4], [0.6, 0.1, 0.3], [0.4, 0.4, 0.2]],
          [[0.6, 0.1, 0.3], [0.2, 0.7, 0.1], [0.2, 0.3, 0.5]],
          [[0.8, 0.1, 0.1], [0.2, 0.6, 0.2], [0.4, 0.1, 0.5]],
          [[0.3, 0.6, 0.1], [0.2, 0.5, 0.3], [0.1, 0.7, 0.2]],
          [[0.3, 0.6, 0.1], [0.5, 0.4, 0.1], [0.5, 0.3, 0.2]],
          [[0.3, 0.1, 0.6], [0.1, 0.5, 0.4], [0.3, 0.3, 0.4]],
          [[0.4, 0.4, 0.2], [0.1, 0.1, 0.8], [0.2, 0.6, 0.2]],
          [[0.4, 0.2, 0.4], [0.3, 0.3, 0.4], [0.3, 0.6, 0.1]],
          [[0.3, 0.3, 0.4], [0.2, 0.2, 0.6], [0.1, 0.2, 0.7]],
          [[0.7, 0.2, 0.1], [0.1, 0.3, 0.6], [0.4, 0.2, 0.4]],
          [[0.2, 0.6, 0.2], [0.1, 0.5, 0.4], [0.3, 0.5, 0.2]],
          [[0.2, 0.3, 0.5], [0.1, 0.1, 0.8], [0.1, 0.7, 0.2]],
          [[0.4, 0.2, 0.4], [0.3, 0.1, 0.6], [0.1, 0.6, 0.3]],
          [[0.1, 0.6, 0.3], [0.3, 0.5, 0.2], [0.1, 0.7, 0.2]],
          [[0.2, 0.5, 0.3], [0.2, 0.3, 0.5], [0.2, 0.6, 0.2]],
          [[0.1, 0.1, 0.8], [0.1, 0.7, 0.2], [0.6, 0.3, 0.1]],
          [[0.3, 0.5, 0.2], [0.1, 0.1, 0.8], [0.4, 0.2, 0.4]],
          [[0.1, 0.2, 0.7], [0.1, 0.4, 0.5], [0.3, 0.5, 0.2]],
          [[0.7, 0.2, 0.1], [0.4, 0.1, 0.5], [0.5, 0.1, 0.4]],
          [[0.3, 0.4, 0.3], [0.1, 0.1, 0.8], [0.3, 0.1, 0.6]],
          [[0.6, 0.3, 0.1], [0.5, 0.4, 0.1], [0.5, 0.1, 0.4]],
          [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.2, 0.1, 0.7]],
          [[0.1, 0.1, 0.8], [0.4, 0.2, 0.4], [0.3, 0.1, 0.6]],
          [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.3, 0.2, 0.5]],
          [[0.2, 0.3, 0.5], [0.1, 0.5, 0.4], [0.5, 0.3, 0.2]],
          [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.4, 0.5, 0.1]],
          [[0.2, 0.1, 0.7], [0.4, 0.2, 0.4], [0.7, 0.2, 0.1]],
          [[0.2, 0.5, 0.3], [0.6, 0.3, 0.1], [0.2, 0.6, 0.2]],
          [[0.1, 0.1, 0.8], [0.7, 0.2, 0.1], [0.5, 0.3, 0.2]],
          [[0.4, 0.1, 0.5], [0.1, 0.5, 0.4], [0.1, 0.3, 0.6]],
          [[0.4, 0.2, 0.4], [0.2, 0.4, 0.4], [0.5, 0.3, 0.2]],
          [[0.4, 0.3, 0.3], [0.6, 0.1, 0.3], [0.7, 0.2, 0.1]],
          [[0.1, 0.8, 0.1], [0.5, 0.4, 0.1], [0.4, 0.5, 0.1]],
          [[0.2, 0.4, 0.4], [0.3, 0.1, 0.6], [0.6, 0.1, 0.3]],
          [[0.8, 0.1, 0.1], [0.2, 0.4, 0.4], [0.2, 0.2, 0.6]],
          [[0.6, 0.1, 0.3], [0.2, 0.4, 0.4], [0.2, 0.3, 0.5]],
          [[0.2, 0.2, 0.6], [0.4, 0.5, 0.1], [0.1, 0.5, 0.4]],
          [[0.2, 0.5, 0.3], [0.3, 0.5, 0.2], [0.6, 0.2, 0.2]],
          [[0.1, 0.5, 0.4], [0.7, 0.2, 0.1], [0.2, 0.2, 0.6]],
          [[0.2, 0.3, 0.5], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
          [[0.3, 0.2, 0.5], [0.3, 0.6, 0.1], [0.4, 0.4, 0.2]],
          [[0.4, 0.3, 0.3], [0.4, 0.2, 0.4], [0.6, 0.2, 0.2]],
          [[0.1, 0.3, 0.6], [0.3, 0.2, 0.5], [0.1, 0.1, 0.8]],
          [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.2, 0.5, 0.3]],
          [[0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.1, 0.5, 0.4]],
          [[0.2, 0.6, 0.2], [0.1, 0.1, 0.8], [0.4, 0.2, 0.4]],
          [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.6, 0.1, 0.3]],
          [[0.5, 0.1, 0.4], [0.1, 0.7, 0.2], [0.3, 0.2, 0.5]],
          [[0.1, 0.6, 0.3], [0.4, 0.2, 0.4], [0.2, 0.1, 0.7]],
          [[0.1, 0.5, 0.4], [0.5, 0.1, 0.4], [0.3, 0.5, 0.2]],
          [[0.6, 0.3, 0.1], [0.1, 0.8, 0.1], [0.2, 0.3, 0.5]],
          [[0.5, 0.3, 0.2], [0.2, 0.4, 0.4], [0.3, 0.2, 0.5]],
          [[0.2, 0.4, 0.4], [0.1, 0.6, 0.3], [0.8, 0.1, 0.1]],
          [[0.3, 0.3, 0.4], [0.2, 0.3, 0.5], [0.4, 0.3, 0.3]],
          [[0.3, 0.3, 0.4], [0.6, 0.3, 0.1], [0.2, 0.6, 0.2]],
          [[0.1, 0.7, 0.2], [0.1, 0.4, 0.5], [0.5, 0.3, 0.2]],
          [[0.4, 0.1, 0.5], [0.5, 0.4, 0.1], [0.5, 0.2, 0.3]],
          [[0.3, 0.1, 0.6], [0.5, 0.1, 0.4], [0.1, 0.3, 0.6]],
          [[0.6, 0.2, 0.2], [0.3, 0.4, 0.3], [0.2, 0.3, 0.5]],
          [[0.1, 0.5, 0.4], [0.3, 0.3, 0.4], [0.2, 0.4, 0.4]],
          [[0.5, 0.4, 0.1], [0.3, 0.6, 0.1], [0.6, 0.3, 0.1]],
          [[0.4, 0.1, 0.5], [0.7, 0.2, 0.1], [0.5, 0.2, 0.3]],
          [[0.3, 0.4, 0.3], [0.1, 0.3, 0.6], [0.1, 0.8, 0.1]],
          [[0.8, 0.1, 0.1], [0.5, 0.2, 0.3], [0.4, 0.5, 0.1]],
          [[0.3, 0.1, 0.6], [0.3, 0.4, 0.3], [0.2, 0.2, 0.6]],
          [[0.7, 0.1, 0.2], [0.6, 0.2, 0.2], [0.3, 0.5, 0.2]],
          [[0.5, 0.2, 0.3], [0.7, 0.2, 0.1], [0.4, 0.4, 0.2]],
          [[0.7, 0.1, 0.2], [0.4, 0.5, 0.1], [0.2, 0.6, 0.2]],
          [[0.5, 0.4, 0.1], [0.2, 0.1, 0.7], [0.8, 0.1, 0.1]],
          [[0.2, 0.1, 0.7], [0.6, 0.3, 0.1], [0.1, 0.4, 0.5]],
          [[0.5, 0.1, 0.4], [0.4, 0.4, 0.2], [0.4, 0.3, 0.3]],
          [[0.6, 0.2, 0.2], [0.8, 0.1, 0.1], [0.3, 0.4, 0.3]],
          [[0.4, 0.3, 0.3], [0.3, 0.6, 0.1], [0.5, 0.1, 0.4]],
          [[0.7, 0.1, 0.2], [0.2, 0.4, 0.4], [0.5, 0.1, 0.4]],
          [[0.2, 0.7, 0.1], [0.2, 0.4, 0.4], [0.5, 0.4, 0.1]],
          [[0.1, 0.8, 0.1], [0.6, 0.1, 0.3], [0.5, 0.4, 0.1]],
          [[0.3, 0.4, 0.3], [0.1, 0.2, 0.7], [0.4, 0.5, 0.1]],
          [[0.1, 0.1, 0.8], [0.5, 0.3, 0.2], [0.2, 0.1, 0.7]],
          [[0.4, 0.2, 0.4], [0.1, 0.6, 0.3], [0.2, 0.3, 0.5]],
          [[0.7, 0.1, 0.2], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
          [[0.5, 0.3, 0.2], [0.6, 0.1, 0.3], [0.4, 0.4, 0.2]],
          [[0.2, 0.3, 0.5], [0.2, 0.6, 0.2], [0.6, 0.2, 0.2]],
          [[0.5, 0.2, 0.3], [0.5, 0.3, 0.2], [0.3, 0.1, 0.6]],
          [[0.1, 0.2, 0.7], [0.1, 0.7, 0.2], [0.7, 0.2, 0.1]],
          [[0.1, 0.3, 0.6], [0.3, 0.5, 0.2], [0.2, 0.7, 0.1]],
          [[0.1, 0.8, 0.1], [0.2, 0.1, 0.7], [0.4, 0.1, 0.5]],
          [[0.1, 0.8, 0.1], [0.1, 0.7, 0.2], [0.1, 0.5, 0.4]],
          [[0.2, 0.4, 0.4], [0.1, 0.6, 0.3], [0.5, 0.3, 0.2]],
          [[0.1, 0.7, 0.2], [0.1, 0.8, 0.1], [0.3, 0.4, 0.3]],
          [[0.5, 0.1, 0.4], [0.3, 0.1, 0.6], [0.2, 0.3, 0.5]],
          [[0.1, 0.4, 0.5], [0.5, 0.1, 0.4], [0.1, 0.6, 0.3]],
          [[0.5, 0.1, 0.4], [0.2, 0.4, 0.4], [0.4, 0.3, 0.3]],
          [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.1, 0.1, 0.8]],
          [[0.1, 0.7, 0.2], [0.1, 0.8, 0.1], [0.3, 0.1, 0.6]],
          [[0.1, 0.7, 0.2], [0.6, 0.3, 0.1], [0.2, 0.3, 0.5]],
          [[0.3, 0.2, 0.5], [0.1, 0.1, 0.8], [0.4, 0.4, 0.2]],
          [[0.3, 0.6, 0.1], [0.7, 0.2, 0.1], [0.6, 0.3, 0.1]],
          [[0.3, 0.3, 0.4], [0.5, 0.2, 0.3], [0.4, 0.2, 0.4]],
          [[0.1, 0.6, 0.3], [0.3, 0.1, 0.6], [0.5, 0.1, 0.4]],
          [[0.5, 0.3, 0.2], [0.8, 0.1, 0.1], [0.1, 0.5, 0.4]],
          [[0.1, 0.5, 0.4], [0.5, 0.3, 0.2], [0.2, 0.6, 0.2]],
          [[0.2, 0.4, 0.4], [0.5, 0.3, 0.2], [0.4, 0.1, 0.5]],
          [[0.2, 0.3, 0.5], [0.1, 0.5, 0.4], [0.3, 0.5, 0.2]],
          [[0.4, 0.3, 0.3], [0.7, 0.1, 0.2], [0.1, 0.8, 0.1]],
          [[0.7, 0.2, 0.1], [0.4, 0.5, 0.1], [0.6, 0.1, 0.3]],
          [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.1, 0.4, 0.5]],
          [[0.1, 0.2, 0.7], [0.2, 0.4, 0.4], [0.1, 0.3, 0.6]],
          [[0.1, 0.8, 0.1], [0.1, 0.3, 0.6], [0.6, 0.3, 0.1]],
          [[0.8, 0.1, 0.1], [0.4, 0.2, 0.4], [0.4, 0.5, 0.1]],
          [[0.5, 0.2, 0.3], [0.1, 0.4, 0.5], [0.1, 0.1, 0.8]],
          [[0.1, 0.8, 0.1], [0.1, 0.3, 0.6], [0.5, 0.1, 0.4]],
          [[0.5, 0.2, 0.3], [0.4, 0.3, 0.3], [0.3, 0.2, 0.5]],
          [[0.4, 0.3, 0.3], [0.7, 0.1, 0.2], [0.1, 0.7, 0.2]],
          [[0.2, 0.3, 0.5], [0.2, 0.7, 0.1], [0.2, 0.2, 0.6]],
          [[0.2, 0.6, 0.2], [0.3, 0.6, 0.1], [0.4, 0.3, 0.3]],
          [[0.2, 0.6, 0.2], [0.1, 0.2, 0.7], [0.5, 0.1, 0.4]],
          [[0.4, 0.4, 0.2], [0.1, 0.2, 0.7], [0.3, 0.1, 0.6]],
          [[0.5, 0.3, 0.2], [0.2, 0.2, 0.6], [0.4, 0.4, 0.2]],
          [[0.5, 0.1, 0.4], [0.5, 0.4, 0.1], [0.6, 0.2, 0.2]],
          [[0.3, 0.1, 0.6], [0.1, 0.3, 0.6], [0.4, 0.1, 0.5]],
          [[0.1, 0.8, 0.1], [0.4, 0.4, 0.2], [0.3, 0.2, 0.5]],
          [[0.3, 0.2, 0.5], [0.5, 0.1, 0.4], [0.1, 0.3, 0.6]],
          [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
          [[0.7, 0.2, 0.1], [0.1, 0.3, 0.6], [0.4, 0.2, 0.4]],
          [[0.1, 0.8, 0.1], [0.6, 0.3, 0.1], [0.4, 0.5, 0.1]],
          [[0.3, 0.1, 0.6], [0.4, 0.1, 0.5], [0.5, 0.3, 0.2]],
          [[0.5, 0.1, 0.4], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
          [[0.1, 0.3, 0.6], [0.6, 0.2, 0.2], [0.8, 0.1, 0.1]],
          [[0.1, 0.3, 0.6], [0.6, 0.3, 0.1], [0.5, 0.3, 0.2]],
          [[0.1, 0.7, 0.2], [0.1, 0.1, 0.8], [0.2, 0.4, 0.4]],
          [[0.5, 0.1, 0.4], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1]],
          [[0.2, 0.2, 0.6], [0.1, 0.7, 0.2], [0.4, 0.4, 0.2]],
          [[0.5, 0.2, 0.3], [0.2, 0.1, 0.7], [0.2, 0.4, 0.4]],
          [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.2, 0.2, 0.6]],
          [[0.1, 0.3, 0.6], [0.1, 0.8, 0.1], [0.6, 0.2, 0.2]],
          [[0.2, 0.3, 0.5], [0.3, 0.6, 0.1], [0.1, 0.6, 0.3]],
          [[0.2, 0.5, 0.3], [0.2, 0.4, 0.4], [0.6, 0.1, 0.3]],
          [[0.2, 0.6, 0.2], [0.6, 0.3, 0.1], [0.1, 0.5, 0.4]],
          [[0.5, 0.2, 0.3], [0.6, 0.2, 0.2], [0.4, 0.3, 0.3]],
          [[0.4, 0.3, 0.3], [0.1, 0.3, 0.6], [0.4, 0.1, 0.5]],
          [[0.2, 0.4, 0.4], [0.8, 0.1, 0.1], [0.1, 0.7, 0.2]],
          [[0.1, 0.5, 0.4], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1]],
          [[0.2, 0.2, 0.6], [0.3, 0.4, 0.3], [0.2, 0.3, 0.5]],
          [[0.5, 0.2, 0.3], [0.3, 0.3, 0.4], [0.1, 0.6, 0.3]],
          [[0.1, 0.8, 0.1], [0.4, 0.2, 0.4], [0.1, 0.6, 0.3]],
          [[0.4, 0.3, 0.3], [0.8, 0.1, 0.1], [0.6, 0.2, 0.2]],
          [[0.6, 0.3, 0.1], [0.2, 0.6, 0.2], [0.2, 0.3, 0.5]],
          [[0.4, 0.5, 0.1], [0.7, 0.1, 0.2], [0.2, 0.6, 0.2]],
          [[0.2, 0.4, 0.4], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]],
          [[0.1, 0.4, 0.5], [0.5, 0.4, 0.1], [0.4, 0.3, 0.3]],
          [[0.3, 0.4, 0.3], [0.2, 0.7, 0.1], [0.5, 0.2, 0.3]],
          [[0.1, 0.2, 0.7], [0.4, 0.4, 0.2], [0.3, 0.6, 0.1]],
          [[0.1, 0.7, 0.2], [0.1, 0.5, 0.4], [0.1, 0.4, 0.5]],
          [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.5, 0.2]],
          [[0.3, 0.5, 0.2], [0.1, 0.3, 0.6], [0.2, 0.5, 0.3]],
          [[0.7, 0.1, 0.2], [0.1, 0.5, 0.4], [0.6, 0.3, 0.1]],
          [[0.1, 0.4, 0.5], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
          [[0.7, 0.1, 0.2], [0.2, 0.2, 0.6], [0.2, 0.1, 0.7]],
          [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.3, 0.4]],
          [[0.4, 0.3, 0.3], [0.3, 0.2, 0.5], [0.6, 0.2, 0.2]],
          [[0.4, 0.2, 0.4], [0.2, 0.1, 0.7], [0.3, 0.3, 0.4]],
          [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.4, 0.2, 0.4]],
          [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.2, 0.4, 0.4]],
          [[0.2, 0.4, 0.4], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
          [[0.2, 0.1, 0.7], [0.1, 0.5, 0.4], [0.3, 0.2, 0.5]],
          [[0.3, 0.4, 0.3], [0.5, 0.1, 0.4], [0.4, 0.3, 0.3]],
          [[0.1, 0.5, 0.4], [0.6, 0.3, 0.1], [0.4, 0.3, 0.3]],
          [[0.1, 0.6, 0.3], [0.1, 0.2, 0.7], [0.8, 0.1, 0.1]],
          [[0.1, 0.2, 0.7], [0.2, 0.4, 0.4], [0.2, 0.7, 0.1]],
          [[0.1, 0.4, 0.5], [0.6, 0.1, 0.3], [0.1, 0.3, 0.6]],
          [[0.3, 0.6, 0.1], [0.1, 0.5, 0.4], [0.1, 0.1, 0.8]],
          [[0.1, 0.1, 0.8], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]],
          [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6], [0.3, 0.2, 0.5]],
          [[0.7, 0.1, 0.2], [0.4, 0.5, 0.1], [0.6, 0.2, 0.2]],
          [[0.1, 0.2, 0.7], [0.1, 0.8, 0.1], [0.1, 0.7, 0.2]],
          [[0.1, 0.4, 0.5], [0.1, 0.5, 0.4], [0.2, 0.2, 0.6]],
          [[0.1, 0.1, 0.8], [0.1, 0.8, 0.1], [0.8, 0.1, 0.1]],
          [[0.1, 0.2, 0.7], [0.2, 0.7, 0.1], [0.7, 0.1, 0.2]],
          [[0.1, 0.3, 0.6], [0.3, 0.6, 0.1], [0.6, 0.1, 0.3]],
          [[0.2, 0.1, 0.7], [0.7, 0.2, 0.1], [0.6, 0.1, 0.3]]]

for action in matrix:
    _cursor.execute(_sql_for_task, (action[0][0], action[0][1], action[0][2],
                                    action[1][0], action[1][1], action[1][2],
                                    action[2][0], action[2][1], action[2][2]))
_conn_with_task.commit()
_cursor.close()
_conn_with_task.close()
# for action_index in range(len(matrix)):
#     for row in range(3):
#         for col in range(3):
#             matrix[action_index][row][col] /= 10
# for action_index in matrix:
#     print(str(action_index) + ',')
