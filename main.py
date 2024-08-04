import random

import wx
import drawlots
import repository.sqlit as repo
import utils.excel as ex
from dialogs.data_import_dialog import DataImportDialog
from dialogs.warning_dialog import ErrorWin


# 主窗体
class MainWin(drawlots.main_frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # initialize database
        repo.init_database()
        # initialize table select choices in data panel
        self.refresh_table_choices()
        # data table relevant
        self.table_changed_col = None  # changed cell col index
        self.table_changed_row = None  # changed cell row index
        self.current_grid_page = 1
        # drawing page relevant
        self.drawing_table = None  # 要抽签的表名
        self.base_date_list = None
        self.drawing_num = 0  # 抽取数量
        # drawing result
        self.result = []

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

    # set combo box value TODO
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
            self.drawing_table_combo.Clear()
        tables = repo.get_table_names(inputValue)
        for table in tables:
            self.table_select_combo.Append(table)
            self.drawing_table_combo.Append(table)

    # load selected table data into main grid of data panel
    def load_table_data(self, event):
        clear_grid(self.table_grid)
        # Get current table name
        table_name = self.table_select_combo.GetStringSelection()
        if self.table_select_combo.GetStringSelection() == "":
            print("没选")
            # TODO 提示
            return
        # get table columns first
        columns = repo.get_column_names(table_name)
        # set grid header
        self.table_grid.AppendCols(len(columns))
        self.table_grid.AppendRows(repo.DEFAULT_PAGE_SIZE)
        # retrieve data from database and load data
        load_new_data(self.table_grid, table_name, columns, self.current_grid_page)
        # check page btn status
        total_pages = repo.get_total_pages(table_name)
        if total_pages > 1:
            self.grid_next_page_btn.Enable(True)

    def grid_pre_page(self, event):
        self.current_grid_page = page_pre(self.table_grid, self.current_grid_page,
                                          self.table_select_combo.GetStringSelection())
        if self.current_grid_page == 1:
            self.grid_pre_page_btn.Enable(False)

    def grid_next_page(self, event):
        current = page_next(self.table_grid, self.current_grid_page,
                            self.table_select_combo.GetStringSelection())
        total_pages = repo.get_total_pages(self.table_select_combo.GetStringSelection())
        self.current_grid_page = current
        self.grid_next_page_btn.Enable(current < total_pages)
        self.grid_pre_page_btn.Enable(True)

    # refresh grid
    def refresh_grid_table(self, event):
        # TODO current useless function
        self.load_table_data(event)

    # check operation status
    def on_table_data_select(self, event):
        # handling delete
        if len(self.table_grid.GetSelectedRows()) > 0:
            self.delete_table_data_btn.Enable(True)
            print(self.table_grid.GetSelectedRows())
        else:
            self.delete_table_data_btn.Enable(False)

    # when change data in table
    def on_table_data_change(self, event):
        self.update_table_btn.Enable(True)
        self.table_changed_row = event.GetRow()
        self.table_changed_col = event.GetCol()
        # TODO 暂时只允许修改一个值
        self.table_grid.Enable(False)

    # TODO finish this
    def add_table_data(self, event):
        print("unfinished")

    # delete rows
    def delete_table_data(self, event):
        # TODO Warn before operating
        selected_rows = self.table_grid.GetSelectedRows()
        if len(selected_rows) < 0:
            print("未选中数据")
            # TODO Warn
            return
        # get the header and value of first col for each row
        header = self.table_grid.GetColLabelValue(0)
        values = []
        for row in selected_rows:
            values.append(self.table_grid.GetCellValue(row, 0))
        try:
            repo.delete_data(self.table_select_combo.GetStringSelection(), header, values)
        except Exception as e:
            # TODO warn
            print(e)
            return
        # delete selected data in grid view
        for row in reversed(selected_rows):
            self.table_grid.DeleteRows(row)
        self.delete_table_data_btn.Enable(False)

    # update row
    # TODO 这里默认将第一列作为索引列，且每次只能更新一个值
    def update_table_data(self, event):
        if self.table_changed_col == 0:
            # TODO warn 不允许修改第一列
            self.table_grid.Enable(True)
            self.update_table_btn.Enable(False)
            return
        index_field = self.table_grid.GetColLabelValue(0)
        index_value = self.table_grid.GetCellValue(self.table_changed_row, 0)
        field = self.table_grid.GetColLabelValue(self.table_changed_col)
        new_value = self.table_grid.GetCellValue(self.table_changed_row, self.table_changed_col)
        try:
            repo.update_data(self.table_select_combo.GetStringSelection(),
                             index_field, index_value, field, new_value)
        except Exception as e:
            print(e)
            # TODO warn
            return
        finally:
            self.table_grid.Enable(True)
            self.update_table_btn.Enable(False)
            self.table_changed_row = None
            self.table_changed_col = None

    # >>>>>>>>>>>>>>>>>>>>>>>以下为抽签页面操作<<<<<<<<<<<<<<<<<<<<<
    # drawing page select table
    def confirm_draw_table(self, event):
        clear_grid(self.base_data_view)
        # Get all columns
        self.drawing_table = self.drawing_table_combo.GetStringSelection()
        columns = repo.get_column_names(self.drawing_table)
        total = repo.get_total(self.drawing_table)
        # set grid header
        self.base_data_view.AppendCols(len(columns))
        self.base_data_view.AppendRows(total)
        load_all_data(self.base_data_view, self.drawing_table, columns)
        # set drawing btn status
        self.drawing_btn.Enable(True)

    # do drawing operation
    def do_drawing(self, event):
        if self.drawing_num_ctrl.GetValue() <= 0:
            err_win = ErrorWin(self, "抽取数量需要大于0")
            err_win.Show()
            return
        # clear result pool
        self.result = []
        clear_grid(self.result_view)
        # retrieve all data
        table_name = self.drawing_table_combo.GetStringSelection()
        columns = repo.get_column_names(table_name)
        base_data = repo.query_all(table_name, ",".join(columns))
        self.result = random.sample(base_data, self.drawing_num_ctrl.GetValue())
        # add results into view
        self.result_view.AppendCols(len(columns))
        self.result_view.AppendRows(self.drawing_num_ctrl.GetValue())
        add_data_into_grid(self.result_view, columns, self.result)
        # disable drawing button
        self.drawing_btn.Enable(False)
        self.export_result_btn.Enable(True)

    # export result data
    def export_result(self, event):
        dlg = wx.DirDialog(self, message="选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            columns = repo.get_column_names(self.drawing_table)
            res_data = ex.table_list_to_dict(columns, self.result)
            selected_path = dlg.GetPath()
            ex.export_to_excel(f"{self.drawing_table}抽取结果", selected_path, res_data)
            dlg.Close()

    # restart the drawing panel
    def restart_panel(self, event):
        self.drawing_btn.Enable(False)
        self.export_result_btn.Enable(False)
        clear_grid(self.result_view)


# 翻页-上一页
def page_pre(grid, current: int, tableName: str) -> int:
    grid.ClearGrid()
    if current > 1:
        columns = repo.get_column_names(tableName)
        current = current - 1
        load_new_data(grid, tableName, columns, current)
    return current


# 翻页-下一页
def page_next(grid, current: int, tableName: str) -> int:
    current = current + 1
    columns = repo.get_column_names(tableName)
    load_new_data(grid, tableName, columns, current)
    return current


# Clear all data include header
def clear_grid(grid):
    if grid.GetNumberCols() > 0:
        grid.DeleteCols(0, grid.GetNumberCols())
    if grid.GetNumberRows() > 0:
        grid.DeleteRows(0, grid.GetNumberRows())


# 加载数据到grid中
def load_new_data(grid, tableName: str, columns: list, pageNum: int):
    # retrieve data from database and load data
    data = repo.query_page(tableName, ",".join(columns), pageNum, repo.DEFAULT_PAGE_SIZE)
    add_data_into_grid(grid, columns, data)


def load_all_data(grid, tableName: str, columns: list):
    data = repo.query_all(tableName, ",".join(columns))
    add_data_into_grid(grid, columns, data)


def add_data_into_grid(grid, columns: list, data: list):
    for idx, column in enumerate(columns):
        grid.SetColLabelValue(idx, column)
    for row_idx, row_data in enumerate(data):
        for col_idx, col_data in enumerate(row_data):
            grid.SetCellValue(row_idx, col_idx, str(col_data))


# 以下是wxPython的固定用法
if __name__ == '__main__':
    app = wx.App()

    main_win = MainWin(None)
    main_win.Show()

    app.MainLoop()
