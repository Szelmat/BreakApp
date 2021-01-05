import time
import threading

import wx
from playsound import playsound

from timer_panel import TimerPanel


class InfoPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = wx.GridSizer(1)

        #font = wx.Font(13, wx.FONTFAMILY_DEFAULT,
        #    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT)

        self.title_label = wx.StaticText(self, label="")
        # self.title_label.SetFont(font)
        self.layout.Add(self.title_label, wx.ID_ANY, wx.ALIGN_CENTER)

        self.timer_label = wx.StaticText(self, label="")
        # self.timer_label.SetFont(font)
        self.layout.Add(self.timer_label, wx.ID_ANY, wx.ALIGN_CENTER)

        self.progressbar = wx.Gauge(self)
        self.layout.Add(self.progressbar, wx.ID_ANY, wx.ALIGN_CENTER)

        self.SetSizer(self.layout)

    def alarm(self, desc: str) -> bool:
        '''Play the alarm sound and display the prompt'''
        self.change_info(desc)
        playsound("res/sound/alarm.wav")
        self.change_info(desc)
        pb_thread = threading.Thread(target=self.timeout, daemon=True)
        pb_thread.start()
        pb_thread.join()
        self.change_info('')

    def change_info(self, desc: str):
        '''Change the text over the progressbar and center it'''
        self.title_label.SetLabel(desc)
        self.layout.Layout()

    def timeout(self):
        i = 0.1
        while(i < 3):
            self.progressbar.SetValue(3 / i * 100)
            time.sleep(0.1)
            i += 0.1
        self.progressbar.SetValue(0)
