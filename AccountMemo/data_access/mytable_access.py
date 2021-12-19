import sqlite3
from dataclasses import dataclass 

import sql.sql_Mydb as sql

# DBの接続と解除
@dataclass
class DbConnection:
    dbfile_path:str

    def __post_init__(self):
        self.conn = sqlite3.connect(self.dbfile_path)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def comit(self):
        self.conn.commit()
        self.close()

    def rollback(self):
        self.conn.rollback()
        self.close()

def check_table(cur):
    '''
    テーブルの存在確認。
    Args:
        cur(object):カーソルオブジェクト
    Returns:
        result(int):テーブルが存在すれば1、なければ0
    '''
    # テーブルが存在する場合は1を返す
    for row in cur.execute(sql.check_MyTable):
        result = row[0]
    return result
    

def create_table(cur):
    '''
    テーブル作成。
    Args:
        cur(object):カーソルオブジェクト
    Returns:
        result(int):結果
    '''
    query = sql.create_MyTable
    result = 0
    try:
        cur.execute(query)
        print("テーブルを作成しました。")
    except sqlite3.OperationalError as e:
        print("テーブル作成エラー：" + str(e))
        result = 1
    return result

def create_table_init(cur):
    '''
    テーブル作成。
    Args:
        cur(object):カーソルオブジェクト
    Returns:
        result(int):結果
    '''
    result = 0
    if check_table(cur) == 0:
        result = create_table(cur)
    return result

def add_data(cur,value_tuple):
    '''
    テーブルデータを追加。
    Args:
        cur(object):カーソルオブジェクト
        value_tuple(tuple):挿入する値
    Returns:
        result(int):結果
    '''
    query = sql.add_MyTable
    result = 0
    try:
        cur.execute(query,value_tuple)
        print("データを追加しました。")
    except sqlite3.OperationalError as e:
        print("追加エラー：" + str(e))
        result = 2
    except sqlite3.IntegrityError as e:
        print("すでにデータが存在します：" + str(e))
        result = 1
    return result

def get_data(cur,value_tuple):
    '''
    テーブルの「name」か「url」と一致するデータ取得。
    Args:
        cur(object):カーソルオブジェクト
        value_tuple(tuple):取得したい値
    Returns:
        result(list):取得結果
    '''
    query = sql.get_MyTable
    result = []
    try:
        cur.execute(query,value_tuple)
        for row in cur:
            result.append(row)
    except sqlite3.OperationalError as e:
        print("データ取得失敗：" + str(e))
    return result

def get_check_data(cur,value_tuple):
    '''
    テーブルの「name」と「url」が一致するデータを1つ取得。
    Args:
        cur(object):カーソルオブジェクト
        value_tuple(tuple):取得したい値
    Returns:
        result(list):取得結果
    '''
    query = sql.get_only_MyTable
    result = []
    try:
        cur.execute(query,value_tuple)
        for row in cur:
            result.append(row)
    except sqlite3.OperationalError as e:
        print("データ取得失敗：" + str(e))
    return result

def get_all_data(cur):
    '''
    テーブルの全てのデータを取得。
    Args:
        cur(object):カーソルオブジェクト
    Returns:
        result(list):取得結果
    '''
    query = sql.get_all_MyTable
    result = []
    try:
        cur.execute(query)
        for row in cur:
            result.append(row)
    except sqlite3.OperationalError as e:
        print("データ取得失敗：" + str(e))
    return result

def update_data(cur,value_tuple):
    '''
    レコードの更新。
    Args:
        cur(object):カーソルオブジェクト
        value_tuple(tuple):更新する値
    Returns:
        result(int):更新結果
    '''
    query = sql.update_Mytable
    result = 0
    try:
        check_date = (value_tuple[5],value_tuple[6])
        if not(get_check_data(cur,check_date)):
            raise Exception
        cur.execute(query,value_tuple)
        print("データを更新しました。")
    except sqlite3.OperationalError as e:
        print("更新エラー：" + str(e))
        result = 2
    except Exception:
        print("更新対象が存在しないか、または既に登録されています。：" + str(check_date))
        result = 1
    return result

def delete_data(cur,value_tuple):
    '''
    レコードの削除。
    Args:
        cur(object):カーソルオブジェクト
        value_tuple(tuple):削除する値
    Returns:
        result(int):削除結果
    '''
    query = sql.delete_Mytable
    result = 0
    try:
        if not(get_check_data(cur,value_tuple)):
            raise Exception
        cur.execute(query,value_tuple)
        print("データを削除しました。")
    except sqlite3.OperationalError as e:
        print("削除エラー：" + str(e))
        result = 2
    except Exception as e:
        print("削除対象が存在しません：" + str(value_tuple))
        result = 1
    return result


