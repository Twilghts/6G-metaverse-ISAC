import psycopg2

if __name__ == '__main__':
    _conn_initialize = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="rkw2536153"
    )
    _cursor = _conn_initialize.cursor()
    _update_keyvalue_dataid = "UPDATE keyvalues " \
                              "SET delay = COALESCE((SELECT max(id) FROM data), 0)" \
                              " WHERE key = 'dataid'"
    _update_keyvalue_taskid = "UPDATE keyvalues " \
                              "SET delay = COALESCE((SELECT max(id) FROM task), 0) " \
                              "WHERE key = 'taskid'"
    _cursor.execute(_update_keyvalue_dataid)
    _cursor.execute(_update_keyvalue_taskid)
