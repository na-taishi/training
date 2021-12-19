import os

import data_access.mytable_access as access


def create_dbdata_path(dir_name,db_name):
    '''
    DBのデータファイルのパスを作成する。
    Args:
        dir_name(string):カレントと結合するディレクトリ名称
        db_name(string):カレントと結合するファイル名称
    Returns:
        path(string):作成したパス
    '''
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(current_dir,dir_name)
    path = os.path.join(dir_path,db_name)
    return path

def instantiate_mydb():
    '''
    Mydbの接続クラスのインスタンス化。
    Returns:
        mydb(class):インスタンス化したクラス
    '''
    # DBファイルパス作成
    dir_name = "dbdata"
    db_name = "Mydb"
    dbfile_path = create_dbdata_path(dir_name,db_name)
    # Mydbの接続クラスのインスタンス化
    mydb = access.DbConnection(dbfile_path)
    return mydb

def start_mydb():
    '''
    テーブルを作成する(アプリ開始時に実行する)。
    Returns:
        result(int):エラー時に1を出力
    '''
    mydb = instantiate_mydb()
    result = access.create_table_init(mydb.cur)
    mydb.close()
    return result

def add_record(value_tuple):
    '''
    テーブルにデータを追加する。
    Args:
        value_tuple(tuple):追加するデータ
    Returns:
        result(int):エラー時に1を出力
    '''
    mydb = instantiate_mydb()
    result = access.add_data(mydb.cur,value_tuple)
    mydb.comit()
    return result

def update_record(value_tuple):
    '''
    テーブルのデータを更新する。
    Args:
        value_tuple(tuple):追加するデータ
    Returns:
        result(int):エラー時に1を出力
    '''
    mydb = instantiate_mydb()
    result = access.update_data(mydb.cur,value_tuple)
    mydb.comit()
    return result

def delete_record(value_tuple):
    '''
    テーブルのデータを更新する。
    Args:
        value_tuple(tuple):追加するデータ
    Returns:
        result(int):エラー時に1を出力
    '''
    mydb = instantiate_mydb()
    result = access.delete_data(mydb.cur,value_tuple)
    mydb.comit()
    return result

def get_record(value_tuple):
    '''
    テーブルの条件の一致するデータを検索する。
    Args:
        value_tuple(tuple):検索するデータの条件
    Returns:
        result(list):取得結果
    '''
    mydb = instantiate_mydb()
    result = access.get_data(mydb.cur,value_tuple)
    mydb.close()
    return result

def get_all_record():
    '''
    テーブルのデータを全て検索する。
    Returns:
        result(list):取得結果
    '''
    mydb = instantiate_mydb()
    result = access.get_all_data(mydb.cur)
    mydb.close()
    return result