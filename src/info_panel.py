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

        self.cont = False

        self.SetSizer(self.layout)

    def alarm(self, desc: str) -> bool:
        '''Play the alarm sound and display the prompt'''
        self.change_info(desc)
        try:
            playsound("res/sound/alarm.wav")
        except Exception:
            playsound("../res/sound/alarm.wav")
        self.change_info(desc)

        self.cont = False
        pb_thread = threading.Thread(target=self.timeout, daemon=True)
        pb_thread.start()
        pb_thread.join()
        self.change_info('')

    def change_info(self, desc: str):
        '''Change the text over the progressbar and center it'''
        self.next_button = wx.Button(self, wx.ID_ANY, label="Next")
        self.layout.Add(self.next_button, wx.ID_ANY, wx.ALIGN_CENTER)
        self.next_button.Bind(wx.EVT_BUTTON, self.next_button_clicked)
        self.title_label.SetLabel(desc)
        self.layout.Layout()

    def next_button_clicked(self):
        self.cont = True

    def timeout(self):
        while(True):
            if self.cont:
                break
            time.sleep(1)
