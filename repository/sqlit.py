import sqlite3

DATABASE = 'lottery.db'
KEY_SQL = "ID INTEGER PRIMARY KEY AUTOINCREMENT"
DEFAULT_PAGE_SIZE = 50


# initialize the database, if lottery.db has been created
def init_database():
    conn = sqlite3.connect(DATABASE)
    conn.close()


# create new table
# TODO should let user decide which sheet to import
# noinspection SqlDialectInspection
def create_table(tableName: str, columns: list):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    if len(columns) <= 0:
        raise Exception(f"没有有效的列名")

    # check if the table already exists
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}'")
    exists = cur.fetchone()
    if exists:
        raise Exception(f"表格: {tableName}已存在，请修改表格名称")
    cols_sql = KEY_SQL
    for column in columns:
        cols_sql += f",\n {column}     TEXT"
    try:
        cur.execute(f"CREATE TABLE {tableName} (\n{cols_sql});")
    except Exception as e:
        raise Exception(f"创建数据表:{tableName}失败: {e}")


# as function name
def insert_data(tableName: str, columns: list, values):
    if len(columns) <= 0 or len(values) <= 0:
        raise Exception(f"表格{tableName}要导入的数据为空")
    # assembly sql
    column_str = ",".join(columns)
    placeholder = ', '.join(['?'] * len(columns))
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.executemany(f"INSERT INTO {tableName} ({column_str}) VALUES ({placeholder})", values)
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"表格{tableName}数据导入失败: {e}")


# retrieve all table names
def get_table_names(tableName: str = None) -> list:
    tables = []
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        if tableName is not None:
            sql += f" AND name LIKE '%{tableName}%'"
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            # remove the default table of sqlite
            if result[0] != 'sqlite_sequence':
                tables.append(result[0])
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"查询表格数据失败: {e}")
    return tables


# query page data from certain table
def query_page(tableName: str, columns: str, pageNum: int, pageSize: int):
    # if tableName is None:
    #    return None
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    sql = f"SELECT {columns} FROM {tableName} ORDER BY ID ASC LIMIT {pageSize} OFFSET {pageSize * (pageNum - 1)}"
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results


# query all data from a table
def query_all(tableName: str, columns: str):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    sql = f"SELECT {columns} FROM {tableName}"
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results


# get column names from certain table
def get_column_names(tableName: str) -> list:
    column_names = []
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({tableName})")
    columns_info = cur.fetchall()
    conn.close()
    for column in columns_info:
        if column[1] != 'ID':
            column_names.append(column[1])
    return column_names


# delete data
def delete_data(tableName: str, column: str, values: list):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {tableName} WHERE {column} IN ('{','.join(values)}')")
    conn.commit()
    conn.close()


# update single value
def update_data(tableName: str, index_column: str, index_value, column: str, value):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(f"UPDATE {tableName} SET {column} = '{value}' WHERE {index_column} = '{index_value}'")
    conn.commit()
    conn.close()


def get_total_pages(tableName: str) -> int:
    return int(get_total(tableName) / DEFAULT_PAGE_SIZE)


def get_total(tableName: str) -> int:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {tableName}")
    total = cur.fetchone()[0]
    conn.close()
    return total
