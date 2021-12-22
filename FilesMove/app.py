import os
import configparser
import shutil
import glob
import sys

#パス作成
def join_path(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    join_path = os.path.join(current_dir,name)
    return join_path

#設定ファイルから各種設定を取得
def get_items_list(config,sectionname):
    items_list = config.items(sectionname)
    return items_list

#ディレクトリ作成(すでにある場合作成しない)
def make_dir(items_list):
    flg = False
    for item in items_list:
        os.makedirs(item[1], exist_ok=True)
        #ディレクトリが存在しない場合はアプリを終了させる
        flg = os.path.exists(item[1])
        if(flg == False):
            break
    return flg

#ファイル名を指定した文字列ごとに分けて取得
def get_filenames_list(target_path,items_list):
    paths = os.path.join(target_path,"*")
    filenames_list = []
    tmp_filenames = []
    for file in glob.glob(paths):
        tmp_filenames.append(os.path.split(file)[1])
    for item in items_list:
        #設定ファイルのデータと部分一致するものを抜き出す
        filenames = [filename for filename in tmp_filenames if item[0] in filename]
        #データが重複しないように抜き出したものはリストから削除する
        tmp_filenames = list(filter(lambda x: x not in filenames, tmp_filenames))
        #リストの先頭にパスをセット
        filenames.insert(0,item[1])
        filenames_list.append(filenames)
    return filenames_list

#ファイル移動
def move_file(target_path,output_items_list):
    for output_items in output_items_list:
        for i in range(1,len(output_items)):
            move_file = os.path.join(output_items[0],output_items[i])
            target_file = os.path.join(target_path,output_items[i])
            print(target_file + "を" + move_file + "へ移動しました。")            
            shutil.move(target_file,move_file)
    return 0

def main():
    #ファイル名とディレクトリ名
    config_filename = "config.ini"
    section1 = "TARGETDIR"
    section2 = "OUTPUT"

    #設定ファイル読み込み
    config = configparser.ConfigParser()
    configpath = join_path(config_filename)
    config.read(configpath,"utf8")
    items_list = get_items_list(config,section2)
    target_path = config.items(section1)[0][1]
    #ディレクトリ作成
    check_flg = make_dir(items_list)
    if(check_flg == False):
        print(1)
        sys.exit()
    #ファイルを分別
    filenames_list = get_filenames_list(target_path,items_list)
    #ファイルの移動
    move_file(target_path,filenames_list)
    print("処理を終了します。")

if __name__ == "__main__":
    main()
