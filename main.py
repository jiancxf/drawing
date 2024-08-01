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
        # initialize table select choices in data panel
        self.refresh_table_choices()

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

    # set combo box value
    def choose_table(self, event):
        selection = self.table_select_combo.GetStringSelection()

    # select tables base on user input
    # TODO This gonna influence selection logic
    def filter_table_choices(self, event):
        self.refresh_table_choices(self.table_select_combo.GetValue())

    # refresh table choices
    def refresh_table_choices(self, inputValue: str = None):
        if self.table_select_combo.GetCount() > 0:
            self.table_select_combo.Clear()
        tables = repo.get_table_names(inputValue)
        for table in tables:
            self.table_select_combo.Append(table)

    # load selected table data into main grid of data panel
    def load_table_data(self, event):
        table_name = self.table_select_combo.GetStringSelection()
        if self.table_select_combo.GetStringSelection() == "":
            print("没选")
            # TODO 提示
            return
        # get table columns first
        columns = repo.get_column_names(table_name)
        # retrieve data from database
        data = repo.query_page(table_name, ",".join(columns), 1, repo.DEFAULT_PAGE_SIZE)
        # set grid header and load data
        self.table_grid.AppendCols(len(columns))
        self.table_grid.AppendRows(len(data))
        print(len(data))
        for idx, column in enumerate(columns):
            self.table_grid.SetColLabelValue(idx, column)
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.table_grid.SetCellValue(row_idx, col_idx, str(col_data))


# 以下是wxPython的固定用法
if __name__ == '__main__':
    app = wx.App()

    main_win = MainWin(None)
    main_win.Show()

    app.MainLoop()
