import wx

import drawing


# 主窗体
class MainWin(drawing.main_frame):
    def __init__(self, parent=None):
        super().__init__(parent)


# 以下是wxPython的固定用法
if __name__ == '__main__':
    app = wx.App()

    main_win = MainWin(None)
    main_win.Show()

    app.MainLoop()
