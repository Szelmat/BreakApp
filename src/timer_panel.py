import math
import threading
import time

import wx


class TimerPanel(wx.Panel):
    def __init__(self, parent, name: str, seconds: int):
        super().__init__(parent)
        self.name = name
        self.seconds_original = seconds
        self.seconds = seconds
        self.build_widget()
        self.start_countdown()

    def reset(self):
        """Reset the timer (used after alarm)"""
        self.finished = False
        self.seconds = self.seconds_original
        self.time_label.SetLabel(self.format_time())

    def build_widget(self):
        """Lay out the visual elements of the widget"""
        self.title_label = self.get_title_label()
        self.time_label = self.get_time_label()
        self.layout = wx.GridSizer(1)
        self.layout.Add(self.title_label, wx.ID_ANY, wx.ALIGN_CENTER)
        self.layout.Add(self.time_label, wx.ID_ANY, wx.ALIGN_CENTER)
        self.SetSizer(self.layout)

    def get_title_label(self) -> wx.StaticText:
        """Construct the label corresponding to the timer"""
        label = wx.StaticText(self, label=f"{self.name.title()}")
        return label

    def get_time_label(self) -> wx.StaticText:
        """Construct the label showing the time countdown"""
        label = wx.StaticText(self, label=self.format_time())
        return label

    def format_time(self) -> str:
        """Make the time more readable"""
        hours, mins, secs = self.calculate_time()
        if hours > 0:
            return (f"{str(hours).zfill(2)}:{str(mins).zfill(2)}:"
                    f"{str(secs).zfill(2)}")
        return f"{str(mins).zfill(2)}:{str(secs).zfill(2)}"

    def calculate_time(self) -> list:
        """Calculate the hours, minutes, seconds remaining"""
        if self.seconds == 0:
            return [0, 0, 0]
        hours_minutes_seconds = []
        hours = math.floor(self.seconds / 3600)
        hours_minutes_seconds.append(hours)
        hours_minutes_seconds.append(
            math.floor(self.seconds / 60) - hours * 60)
        hours_minutes_seconds.append(self.seconds % 60)
        return hours_minutes_seconds

    def start_countdown(self):
        """Construct a new countdown loop and start it"""
        self.reset()
        self.countdown_thread = threading.Thread(target=self.countdown,
                                                 daemon=True)
        self.finished = False
        self.countdown_thread.start()

    def countdown(self):
        """Construct and start the countdown loop"""
        self.seconds = self.seconds_original
        while True:
            self.seconds -= 1
            self.time_label.SetLabel(self.format_time())
            self.Layout()
            time.sleep(1)
            if self.seconds <= 0:
                self.finished = True
                return
