from dataclasses import dataclass
from dataclasses import field

import PySimpleGUI as sg

import logic.db_ctr as db
import logic.view_ctr as view


# 画面の親クラス
@dataclass
class WindowClass:
    # sg.theme('Dark Blue 3')
    name:str
    size_x:int = 800
    size_y:int = 400
    layout:list = field(default_factory=list)
    window = None

    # インスタンス生成時に画面を作成
    def __post_init__(self):
        self.window = sg.Window(self.name,self.layout,size=(self.size_x,self.size_y))

# メイン画面
@dataclass
class TopWindow(WindowClass):
    name:str = "TOP"
    layout:list = field(default_factory=lambda:[ 
        [sg.Text(("RegistrationName OR URL"),size=(30,1)),sg.InputText(),sg.Button("SEARCH"),sg.Button("LIST")],
        [sg.Button("ADD"),sg.Button("CANCEL")]
    ]
    )

    def startup(self):
        while True:
            event,values = self.window.read()
            if event == "SEARCH":
                self.window.hide()
                search = (values[0],values[0])
                view.open_list(search)
                self.window.un_hide()
            elif event == "LIST":
                self.window.hide()
                view.open_list(None)
                self.window.un_hide()
            elif event == "ADD":
                self.window.hide()
                view.open_registration()
                self.window.un_hide()
            elif event == sg.WIN_CLOSED or event == "CANCEL":
                break
        self.window.close()

# 一覧画面
@dataclass
class ListWindow(WindowClass):
    name:str = "LIST"
    rows:list =field(default_factory=list)
    header:list =field(default_factory=lambda:["name","url"])

    # インスタンス生成時に画面を作成
    def __post_init__(self):
        self.layout = [[sg.Table(
            self.rows,
            headings=self.header,
            col_widths=[30,100],
            auto_size_columns=False,
            justification="left",
            select_mode=sg.TABLE_SELECT_MODE_BROWSE,
            num_rows=None,
            text_color="#000000",
            background_color="#cccccc",
            alternating_row_color="#ffffff",
            header_text_color="#0000ff",
            header_background_color="#cccccc",
            key="table"
            )],
            [sg.Button("OK"),sg.Button("CANCEL")
            ]]
        self.window = sg.Window(self.name,self.layout,size=(self.size_x,self.size_y))
        

    def startup(self):
        while True:
            event,values = self.window.read()
            if event == "OK":
                if values["table"]:
                    self.window.close()
                    selected = values["table"][0]
                    view.open_detail(selected)
            elif event == sg.WIN_CLOSED or event == "CANCEL":
                break
        self.window.close()

# 登録画面と詳細画面の継承元
@dataclass
class DetailWindowClass(WindowClass):
    row:list = field(default_factory=lambda:list("" for _ in range(5)))
    layout_bt:list = field(default_factory=list)

    # インスタンス生成時に画面を作成
    def __post_init__(self):
        self.layout = [ 
            [sg.Text(("RegistrationName"),size=(30,1)),sg.InputText(self.row[0],size=(90,1))],
            [sg.Text(("URL"),size=(30,1)),sg.InputText(self.row[1],size=(90,1))],
            [sg.Text(("AccountID"),size=(30,1)),sg.InputText(self.row[2],size=(90,1))],
            [sg.Text(("PASSWORD"),size=(30,1)),sg.InputText(self.row[3],size=(90,1))],
            [sg.Text(("MEMO"),size=(30,1)),sg.Multiline(self.row[4],size=(90,15))]
        ]
        self.layout.append(self.layout_bt)
        self.window = sg.Window(self.name,self.layout,size=(self.size_x,self.size_y))

# 登録画面
@dataclass
class RegistrationWindow(DetailWindowClass):
    name:str = "Registration"
    layout_bt:list = field(default_factory=lambda:[sg.Button("REGISTER"),sg.Button("CANCEL")])

    def startup(self):
        while True:
            event,values = self.window.read()
            if event == "REGISTER" and values[0] and values[1]:
                popup = sg.popup_ok_cancel("Do you want to register?")
                if popup == "OK":
                    code = db.add_record(tuple(values.values()))
                    if code == 1:
                        sg.popup("It already exists!")
                    elif code == 0:
                        sg.popup("Completed!")
                        self.window.close()
            elif event == "REGISTER":
                sg.popup("Please enter your RegistrationName and URL!")
            elif event == sg.WIN_CLOSED or event == "CANCEL":
                break
        self.window.close()

# 詳細画面
@dataclass
class DetailWindow(DetailWindowClass):
    name:str = "DETAIL"
    layout_bt:list = field(default_factory=lambda:[sg.Button("UPDATE"),sg.Button("DELETE"),sg.Button("CANCEL")])

    def startup(self):
        while True:
            event,values = self.window.read()
            target = [self.row[0],self.row[1]]
            if event == "UPDATE" and values[0] and values[1]:
                popup = sg.popup_ok_cancel("Do you want to update?")
                if popup == "OK":
                    update_data = tuple(list(values.values()) + target)
                    code = db.update_record(update_data)
                    if code == 1:
                        sg.popup("Do not exist!")
                    elif code == 0:
                        sg.popup("Completed!")
                        self.window.close()
            elif event == "UPDATE":
                sg.popup("Please enter your RegistrationName and URL!")
            elif event == "DELETE":
                code = db.delete_record(tuple(target))
                if code == 1:
                    sg.popup("Do not exist!")
                elif code == 0:
                    sg.popup("DELETE!")
                    self.window.close()
            elif event == sg.WIN_CLOSED or event == "CANCEL":
                break
        self.window.close()
