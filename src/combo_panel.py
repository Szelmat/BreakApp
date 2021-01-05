import time
import threading

import wx

from info_panel import InfoPanel
from timer_panel import TimerPanel

class ComboPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = wx.GridSizer(3)
        self.SetSizer(self.layout)

        self.info_panel = InfoPanel(self)
        self.layout.Add(self.info_panel, wx.ID_ANY, wx.ALIGN_CENTER)

        self.timer_panels = (
            TimerPanel(self, "Relax Eyes", 10),  # 900
            TimerPanel(self, "Rest Hands", 20),  # 2400
            TimerPanel(self, "Stand Up", 3600),
            TimerPanel(self, "Stretch", 7200)
        )

        for panel in self.timer_panels:
            self.layout.Add(panel, wx.ID_ANY, wx.ALIGN_CENTER)

        alarm_checker_thread = threading.Thread(
            target=self.check_alarms, daemon=True)
        alarm_checker_thread.start()

    def check_alarms(self):
        while(True):
            for timer_panel in self.timer_panels:
                if timer_panel.finished:
                    # Bring the window forward
                    self.parent.Raise()
                    self.parent.RequestUserAttention()
                    self.parent.Iconize(False)

                    # Update the UI
                    self.info_panel.alarm(timer_panel.name.title())

                    # Start the new timer
                    timer_panel.start_countdown()
            time.sleep(0.1)
