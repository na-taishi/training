from dataclasses import dataclass

@dataclass
class MytableClass:
    table_data = None
    name:str
    url:str
    id:str
    password:str
    memo:str

    @classmethod
    def save_data(self,rows):
        '''
        構造体のリストを一時的にtable_data変数に保存するクラスメソッド。
        Args:
            rows(list):構造体のリスト
        '''
        MytableClass.table_data = rows

    @classmethod
    def get_table_data(self):
        '''
        table_data変数の中にあるレコードをタプル型からリスト型に変換する。
        Returns:
            (list):リスト型のデータ
        '''
        return  [[row.name,row.url,row.id,row.password,row.memo] for row in MytableClass.table_data]

def convert_dict_from_tuple(tuple_data):
    '''
    MytableClassに対応するタプル型を辞書型に変換する。
    Args:
        tuple_data(tuple):辞書型に変換したいタプル型のデータ
    Returns:
        dict_data(dict):辞書型のデータ
    '''
    key = ["name","url","id","password","memo"]
    val = list(tuple_data)
    dict_data = dict(zip(key, val))
    return dict_data

def convert_mydb_from_tuple(tuple_data):
    '''
    MytableClassに対応するタプル型を構造体に変換する。
    Args:
        tuple_data(tuple):辞書に変換したいタプル型のデータ
    Returns:
        mydb_class(class):構造体のデータ
    '''
    dict_data = convert_dict_from_tuple(tuple_data)
    mydb_class = MytableClass(**dict_data)
    return mydb_class