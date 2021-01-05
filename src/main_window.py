import wx

from combo_panel import ComboPanel

class MainWindow(wx.Frame):
    def __init__(self, window_title):
        super().__init__(
            None, title=window_title, style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER
	        | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX, size=(1000, 700)
        )
        self.Center()

        # Create the menubar and menus
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = file_menu.Append(wx.ID_ANY, '&Reset timers', 'Reset timers')
        menubar.Append(file_menu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.reset_timers, file_item)

        self.panel = ComboPanel(self)
        self.Show()


    def reset_timers(self, e):
        for timer_panel in self.panel.timer_panels:
            timer_panel.reset()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainWindow('BreakApp')
    app.MainLoop()
