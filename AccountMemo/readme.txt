■用途
アカウントを管理

■使用ライブラリ
PySimpleGUI:pip install PySimpleGUI

■使い方
・app.pyを実行
TOP画面
・SEARCHボタン、リスト画面へ遷移（入力フォームに入力した内容を検索）
・LISTボタン、リスト画面へ遷移（登録している全データ表示）
・ADDボタン、登録画面へ遷移
・CANCELボタン、アプリ終了
LIST画面
・OKボタン、選択しているデータの詳細画面へ遷移
・CANCELボタン、TOP画面へ遷移
DETAIL画面
・UPDATEボタン、現在入力している内容に更新
・DELETEボタン、現在見ているデータを削除
・CANCELボタン、TOP画面へ遷移
Registration画面
・REGISTERボタン、現在入力している内容を登録
・CANCELボタン、TOP画面へ遷移
※登録と更新について
・RegistrationNameとURLの入力は必須
・RegistrationNameとURLが既に登録されている場合はエラーになる