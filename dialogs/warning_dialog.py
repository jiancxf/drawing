import drawlots


# 错误提示窗口
class ErrorWin(drawlots.error_dialog):
    def __init__(self, parent, msg="未知错误"):
        super().__init__(parent)
        self.error_message.SetLabelText(msg)

    def err_confirm(self, event):
        self.Destroy()

