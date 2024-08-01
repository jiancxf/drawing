import wx


class TableChangeEvent(wx.PyEvent):
    def __init__(self):
        wx.PyEvent.__init__(self)
        self.SetEventType(TableChangeEventType)


def TableChangeEventType():
    return wx.NewEventType()
