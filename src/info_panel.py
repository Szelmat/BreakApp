import time
import threading

import wx
from playsound import playsound


class InfoPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = wx.GridSizer(1)

        self.layout.Add(wx.StaticText(
            self, label="Current Activity:"), wx.ID_ANY, wx.ALIGN_CENTER)

        self.title_label = wx.StaticText(self, label="")
        self.layout.Add(self.title_label, wx.ID_ANY, wx.ALIGN_CENTER)

        self.progressbar = wx.Gauge(self, size=wx.Size(400, 16))
        self.layout.Add(self.progressbar, wx.ID_ANY, wx.ALIGN_CENTER)

        self.SetSizer(self.layout)

    def alarm(self, desc: str) -> bool:
        '''Play the alarm sound and display the prompt'''
        self.change_info(desc)
        try:
            playsound("res/sound/alarm.wav")
        except Exception:
            playsound("../res/sound/alarm.wav")
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
        seconds_to_wait = 5
        i = 0.1
        while(i < seconds_to_wait):
            self.progressbar.SetValue(seconds_to_wait / i * 100)
            time.sleep(0.1)
            i += 0.1
        self.progressbar.SetValue(0)
