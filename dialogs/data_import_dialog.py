import drawing
import utils.excel as ex


# 数据导入窗口
class DataImportDialog(drawing.import_dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    # on file selected
    def select_data_source(self, event):
        self.file_picker.GetPath()

    # import data from file
    def import_data(self, event):
        ex.resolve_excel(self.file_picker.GetPath())
        self.Destroy()

    # cancel
    def cancel_import_data(self, event):
        self.Destroy()
