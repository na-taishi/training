import logic.db_ctr as db
import view.window as window
import data_access.mytable_access as data_access
import data_access.mytable_record as record


def open_top():
    top = window.TopWindow()
    top.startup()

def open_list(search):
    # DBからデータ取得
    if search:
        rows = db.get_record(search)
    else:
        rows = db.get_all_record()
    # 取得したデータを構造体にして、リストに格納
    struct_list = [record.convert_mydb_from_tuple(row) for row in rows]
    result = [[struct.name,struct.url] for struct in struct_list]
    # 構造体のリストを保存
    record.MytableClass.save_data(struct_list)
    # 画面を開く
    list_window = window.ListWindow(rows=result)
    list_window.startup()

def open_detail(selected):
    # 対象のレコードをリストで取得
    row = record.MytableClass.get_table_data()[selected]
    # 画面を開く
    detail = window.DetailWindow(row=row)
    detail.startup()

def open_registration():
    Registration = window.RegistrationWindow()
    Registration.startup()