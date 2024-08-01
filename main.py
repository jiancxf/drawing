import wx

import repository.sqlit as repo
import drawing
from dialogs.data_import_dialog import DataImportDialog


# 主窗体
class MainWin(drawing.main_frame):
    def __init__(self, parent=None):
        super().__init__(parent)

    # initialize database
    repo.init_database()

    # Open data import dialog
    def show_import_dialog(self, event):
        impt_dialog = DataImportDialog(self)
        impt_dialog.Show(True)

    # 切换至主抽签面板
    def show_main_panel(self, event):
        self.main_panel.Show()
        self.data_panel.Hide()
        self.log_panel.Hide()
        self.data_btn.Enable()
        self.main_btn.Enable(False)
        self.log_btn.Enable()
        self.Layout()

    # 切换至日志面板
    def show_log_panel(self, event):
        self.main_panel.Hide()
        self.data_panel.Hide()
        self.log_panel.Show()
        self.data_btn.Enable()
        self.main_btn.Enable()
        self.log_btn.Enable(False)
        self.Layout()

    # 切换至数据面板
    def show_data_panel(self, event):
        self.main_panel.Hide()
        self.data_panel.Show()
        self.log_panel.Hide()
        self.data_btn.Enable(False)
        self.main_btn.Enable()
        self.log_btn.Enable()
        self.Layout()


# 以下是wxPython的固定用法
if __name__ == '__main__':
    app = wx.App()

    main_win = MainWin(None)
    main_win.Show()

    app.MainLoop()
