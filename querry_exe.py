import sqlite3

def execute_file(file, cur: sqlite3.Cursor, *args, **kwargs):
    with open(file) as f:
        sql = f.read()
        return cur.execute(sql, args).fetchall()


if __name__ == '__main__':
    with sqlite3.connect('univ.db') as conn:
        cur = conn.cursor()
        print(execute_file('query_1.sql', cur))
        print(execute_file('query_2.sql', cur, 1))
        print(execute_file('query_3.sql', cur))
        print(execute_file('query_4.sql', cur))
        print(execute_file('query_5.sql', cur, 1))
        print(execute_file('query_6.sql', cur, 1))
        print(execute_file('query_7.sql', cur, 1, 1))
        print(execute_file('query_8.sql', cur, 1))
        print(execute_file('query_9.sql', cur, 1))
        print(execute_file('query_10.sql', cur, 1, 1))
        print(execute_file('query_11.sql', cur, 1, 1))
        print(execute_file('query_12.sql', cur, 1, 1))
